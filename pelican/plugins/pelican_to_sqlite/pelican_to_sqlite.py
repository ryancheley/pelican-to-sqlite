from datetime import datetime

import html2text
import sqlite_utils

from pelican import signals


def save_items(record: dict, table: str, db: sqlite_utils.Database) -> None:  # pragma: no cover
    try:
        db[table].insert(record, pk="slug", alter=True, replace=True)
    except ZeroDivisionError:
        pass


def create_record(content) -> dict:
    record = {}
    author = content.author.name
    category = content.category.name
    post_content = html2text.html2text(content.content)
    try:
        published_date = content.date.strftime("%Y-%m-%d")
    except AttributeError:
        published_date = datetime.today().strftime("%Y-%m-%d")
    slug = content.slug
    summary = html2text.html2text(content.summary)
    title = content.title
    url = "https://www.ryancheley.com/" + content.url
    status = content.status
    if status == "published":
        record = {
            "author": author,
            "category": category,
            "content": post_content,
            "published_date": published_date,
            "slug": slug,
            "summary": summary,
            "title": title,
            "url": url,
        }
    return record


# Hook function, with the right parameters
def run(gen, content):  # pragma: no cover
    db_name = gen.settings.get("DATABASE", "pelican.db")
    db = sqlite_utils.Database(db_name)
    record = create_record(content)
    save_items(record, "content", db)


# Module entry point
def register():  # pragma: no cover
    # Connect the run hook function to the content_written signal
    signals.article_generator_write_article.connect(run)
    signals.page_generator_write_page.connect(run)
