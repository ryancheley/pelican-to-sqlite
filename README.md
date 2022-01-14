# pelican-to-sqlite

Create a SQLite database containing data posts from your local [pelican](https://blog.getpelican.com) markdown files

## How to install

    $ pip install pelican-to-sqlite

## Usage

    Usage: pelican-to-sqlite [OPTIONS] DBNAME TABLE PATHS...

    Load pelican markdown files into a SQLite database

    DBNAME is the SQLite database to load the data into

    TABLE is the table to load the data into for the specified DBNAME

    PATH is the paths(s) to the markdown files to be loaded


## Using with Datasette

The SQLite database produced by this tool is designed to be browsed using [Datasette](https://datasette.readthedocs.io/). Use the [datasette-render-timestamps](https://github.com/simonw/datasette-render-timestamps) plugin to improve the display of the timestamp values.
