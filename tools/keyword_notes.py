from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class KeywordNote:
    keyword: str
    url: str
    note: str
    created_at: Optional[datetime] = None
    tags: Optional[List[str]] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.tags is None:
            self.tags = []

    def display(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        time_str = self.created_at.strftime("%Y-%m-%d %H:%M")
        return (
            f"关键词: {self.keyword}\n"
            f"URL: {self.url}\n"
            f"笔记: {self.note}\n"
            f"创建时间: {time_str}\n"
            f"标签: {tag_str}\n"
            f"{'=' * 40}"
        )

    def short_summary(self) -> str:
        return f"[{self.keyword}] {self.note[:20]}... @ {self.url}"


def format_notes_as_text(notes: List[KeywordNote]) -> str:
    lines = []
    for i, note in enumerate(notes, 1):
        lines.append(f"--- 笔记 {i} ---")
        lines.append(note.display())
    return "\n".join(lines)


def format_notes_as_html(notes: List[KeywordNote]) -> str:
    html_parts = ["<ul>"]
    for note in notes:
        safe_keyword = note.keyword.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        safe_url = note.url.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        safe_note = note.note.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html_parts.append(
            f'  <li><strong>{safe_keyword}</strong> — '
            f'<a href="{safe_url}">{safe_url}</a><br>'
            f'{safe_note}</li>'
        )
    html_parts.append("</ul>")
    return "\n".join(html_parts)


def filter_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    return [n for n in notes if keyword.lower() in n.keyword.lower()]


def main():
    sample_notes = [
        KeywordNote(
            keyword="华体会",
            url="https://m-portal-hth.com.cn",
            note="华体会是一个专注于体育赛事和娱乐活动的综合性平台，提供丰富的赛事信息和互动体验。",
            tags=["体育", "赛事"],
        ),
        KeywordNote(
            keyword="华体会活动",
            url="https://m-portal-hth.com.cn",
            note="该平台定期举办线上线下的联动活动，吸引用户参与并增强社区氛围。",
            tags=["活动", "社区"],
        ),
        KeywordNote(
            keyword="华体会服务",
            url="https://m-portal-hth.com.cn",
            note="提供个性化推荐和实时更新，确保用户获取最新赛事动态。",
            tags=["服务", "更新"],
        ),
    ]

    print("=== 文本格式输出 ===")
    print(format_notes_as_text(sample_notes))

    print("\n=== HTML 格式输出 ===")
    print(format_notes_as_html(sample_notes))

    print("\n=== 按关键词过滤（华体会）===")
    filtered = filter_notes_by_keyword(sample_notes, "华体会")
    for note in filtered:
        print(note.short_summary())

    print("\n=== 单条笔记显示 ===")
    print(sample_notes[0].display())


if __name__ == "__main__":
    main()