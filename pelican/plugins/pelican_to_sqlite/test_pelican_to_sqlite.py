from pelican.contents import Article
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
