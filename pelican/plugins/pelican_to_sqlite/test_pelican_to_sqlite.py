from datetime import datetime

from pelican.contents import Article, Page
from pelican.urlwrappers import Author, Category
from pelican.utils import SafeDatetime

from .pelican_to_sqlite import create_record


def test_create_record():
    metadata = {
        "author": Author("ryan", settings=None),
        "category": Category("musings", settings=None),
        "date": SafeDatetime.fromisoformat("2016-10-03"),
        "slug": "vins-last-game",
        "summary": "<p>This is the summary</p>",
        "title": "Vin's Last Game",
        "url": "2016/10/03/vins-last-game/",
    }
    content = Article(content="<p>This is the content</p>", metadata=metadata)

    actual = create_record(content)
    expected = {
        "author": "ryan",
        "category": "musings",
        "content": "This is the content\n\n",
        "published_date": "2016-10-03",
        "slug": "vins-last-game",
        "summary": "This is the summary\n\n",
        "title": "Vin's Last Game",
        "url": "https://www.ryancheley.com/2016/10/03/vins-last-game/",
    }
    assert actual == expected


def test_create_record_without_date():
    # Pages are not required to have a date (unlike Articles), and the plugin
    # processes pages too. A dateless page has no `date` attribute, so
    # `content.date` raises AttributeError and create_record falls back to
    # today's date.
    metadata = {
        "author": Author("ryan", settings=None),
        "category": Category("musings", settings=None),
        "slug": "about",
        "summary": "<p>This is the summary</p>",
        "title": "About",
        "url": "pages/about/",
        "status": "published",
    }
    content = Page(content="<p>This is the content</p>", metadata=metadata)

    actual = create_record(content)
    expected = {
        "author": "ryan",
        "category": "musings",
        "content": "This is the content\n\n",
        "published_date": datetime.today().strftime("%Y-%m-%d"),
        "slug": "about",
        "summary": "This is the summary\n\n",
        "title": "About",
        "url": "https://www.ryancheley.com/pages/about/",
    }
    assert actual == expected
