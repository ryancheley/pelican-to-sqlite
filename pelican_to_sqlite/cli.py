import click
from pathlib import Path
import sqlite3
from sqlite_utils import Database
from collections import defaultdict
import hashlib

from .settings import PELICAN_METADATA


def _helper(pelican_metadata, line):
    pelican_metadata_length = len(pelican_metadata)
    pelican_tag = line.split(':', 1)[0].lower()
    if pelican_tag == pelican_metadata:
        return line

@click.command()
@click.version_option()
@click.argument("dbname", nargs=1)
@click.argument("table", nargs=1)
@click.argument("paths", type=click.Path(exists=True), nargs=-1, required=True)
def cli(paths, dbname, table):
    """
    Load pelican markdown files into a SQLite database

    """
    db = Database(dbname)
    docs = []

    for the_file in paths:
        metadata_dictionary = {}
        metadata_dictionary = defaultdict(lambda:None, metadata_dictionary)
        start_line = 0
        with open(the_file) as f:
            lines = f.readlines()
        for line in lines:
            for metadata in PELICAN_METADATA:
                item = _helper(metadata, line)
                if item:
                    start_line += 1
                    metadata_dictionary[item.split(':', 1)[0].lower()] = item.split(':', 1)[1].replace('\n', '')
        if 'save_as' not in metadata_dictionary:
            metadata_dictionary['save_as'] = None
        content = ''.join(lines[start_line:])
        doc = {
            "_id": hashlib.sha1(content.encode("utf8")).hexdigest(),
            "content": content,
            **(metadata_dictionary),
        }
        docs.append(doc)
    columns = list(metadata_dictionary.keys()) + ['_id', 'content']
    db[table].upsert_all(docs, pk="_id")