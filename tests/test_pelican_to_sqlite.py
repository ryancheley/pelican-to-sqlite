import pytest
from pelican_to_sqlite.cli import _helper
from pelican_to_sqlite.settings import PELICAN_METADATA


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