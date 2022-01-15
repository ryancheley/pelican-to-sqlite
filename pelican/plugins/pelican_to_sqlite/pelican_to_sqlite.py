import sqlite_utils

from pelican import signals

DATABASE = "pelican.db"

db = sqlite_utils.Database(DATABASE)


def save_items(record: dict, table: str, db: sqlite_utils.Database) -> None:
    db[table].insert(record, pk="slug", alter=True, replace=True)


# Hook function, with the right parameters
def run(_, content):
    if content.status == "published":
        record = {
            "author": content.author.name,
            "category": content.category.name,
            "content": content.content,
            "published_date": content.date.strftime("%Y-%m-%d"),
            "slug": content.slug,
            "summary": content.summary,
            "title": content.title,
            "url": "https://www.ryancheley.com/" + content.url,
        }
        save_items(record, "content", db)


# Module entry point
def register():
    # Connect the run hook function to the content_written signal
    signals.article_generator_write_article.connect(run)
