import pytest
from click.testing import CliRunner
from sqlite_utils import Database
from pelican_to_sqlite.cli import _helper
from pelican_to_sqlite import cli
from pelican_to_sqlite.settings import PELICAN_METADATA

ONE = """
Title: Not Found
Status: hidden
Save_as: 404.html

The requested item could not be located. 

"""

TWO = """
Title: My Outlook Review Process
Date: 2017-12-30 20:00
Author: ryan
Slug: my-outlook-review-process
Status: published

In a [previous post](/rules-and-actions-in-outlook.html) I spoke about my use of Rules and Custom Actions in Outlook. In this post I’ll talk about my Review process which I adapted from David Allen’s *Getting Things Done* methodology.

"""

def test_basic(tmpdir):
    (tmpdir / "one.md").write(ONE)
    (tmpdir / "two.md").write(TWO)
    result = CliRunner().invoke(
        cli.cli,
        [
            str(tmpdir / "docs.db"),
            "posts",
            str(tmpdir / "one.md"),
            str(tmpdir / "two.md"),
        ],
    )
    db = Database(str(tmpdir / "docs.db"))
    assert ["posts"] == db.table_names()
    assert 2 == db["posts"].count
    one, two = db.execute_returning_dicts("select * from posts")
    assert one["title"] == ' Not Found'
    assert one["status"] == ' hidden'
    assert one["save_as"] == ' 404.html'
    assert one["content"] == "Save_as: 404.html\n\nThe requested item could not be located. \n\n"
    assert two["title"] == ' My Outlook Review Process'
    assert two["date"] == ' 2017-12-30 20:00'
    assert two["author"] == ' ryan'
    assert two["slug"] == ' my-outlook-review-process'
    assert two["status"] == ' published'
    assert two["content"] == "Status: published\n\nIn a [previous post](/rules-and-actions-in-outlook.html) I spoke about my use of Rules and Custom Actions in Outlook. In this post I’ll talk about my Review process which I adapted from David Allen’s *Getting Things Done* methodology.\n\n"
    


def test_helper_true():
    metadata = PELICAN_METADATA[0]
    line = 'Title: This is my title'
    test = _helper(metadata, line)
    assert test

def test_helper_false():
    metadata = PELICAN_METADATA[0]
    line = 'Not_in_metadata: This is my title'
    test = _helper(metadata, line)
    assert not test