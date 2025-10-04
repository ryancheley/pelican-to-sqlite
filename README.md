# pelican-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/pelican-to-sqlite.svg)](https://pypi.org/project/pelican-to-sqlite/)
[![GitHub changelog](https://img.shields.io/github/v/release/ryancheley/pelican-to-sqlite?include_prereleases&label=changelog)](https://github.com/ryancheley/pelican-to-sqlite/releases)
[![Tests](https://github.com/ryancheley/pelican-to-sqlite/workflows/Test/badge.svg)](https://github.com/ryancheley/pelican-to-sqlite/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ryancheley/pelican-to-sqlite/blob/main/LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ryancheley/pelican-to-sqlite/main.svg)](https://results.pre-commit.ci/latest/github/ryancheley/pelican-to-sqlite/main)

## What is pelican-to-sqlite?

pelican-to-sqlite helps you add powerful search capabilities to your Pelican static site. By converting your Pelican posts into a SQLite database, you can quickly search through all your content using Datasette—without needing a complex backend or search service.

Perfect for bloggers and content creators who want to offer visitors an easy way to search through years of posts.

## Prerequisites

- Python 3.8 or higher
- An existing Pelican site
- Basic familiarity with command-line tools

## How to install

### Using uv (recommended)

    uv add pelican-to-sqlite

### Using pip

    pip install pelican-to-sqlite

## Usage

### Configure the Plugin

After installing, add the plugin to your Pelican configuration file (`pelicanconf.py`):

```python
PLUGINS = ['pelican_to_sqlite']
```

### Generate the Database

Run your Pelican build command to create the SQLite database:

```bash
make html
```

This creates a SQLite database called `pelican.db` in the root of your Pelican site, containing all your post data.

### Add Search to Your Site

Add a search form to your `base.html` template (or similar template depending on your theme). Here's an example using [Tailwind CSS](https://tailwindcss.com):

```html
<section class="relative h-8">
    <section class="absolute inset-y-0 right-10 w-128">
        <form class="pl-4" action="your-action-link-here" method="get">
            <label for="site-search">Search the site:</label>
            <input type="search" id="site-search" name="text"
                   aria-label="Search through site content">
            <button class="rounded-full w-16 hover:bg-blue-300">Search</button>
        </form>
    </section>
</section>
```

Replace `your-action-link-here` with the URL from your deployed Datasette instance (see deployment section below).

## Deploy using Vercel

You can deploy your SQLite database with Datasette using several methods. Below is a guide for deploying with Vercel.

> **Note**: The `datasette-publish-vercel` plugin may have limited maintenance. Consider alternative deployment methods like [Datasette Cloud](https://www.datasette.cloud/) or manual Vercel deployment if you encounter issues.

First, install `datasette` using uv (or pip)

```
uv add datasette
# or: pip install datasette
```

Next, install the datasette plugin `datasette-publish-vercel` using uv (or pip)

```
uv add datasette-publish-vercel
# or: pip install datasette-publish-vercel
```

and the [Vercel CLI](https://vercel.com/cli)

Run `vercel login` to log in to (or create) an account.

Publish your `pelican.db` to Vercel by running:

```bash
datasette publish vercel pelican.db
```

For additional publishing options, see the [datasette-publish-vercel documentation](https://github.com/simonw/datasette-publish-vercel/blob/main/README.md).

## Using with Datasette

The SQLite database produced by this tool is designed to be browsed using [Datasette](https://datasette.readthedocs.io/). For a detailed implementation guide, see the blog post [Adding Search to My Pelican Blog with Datasette](https://www.ryancheley.com/2022/01/16/adding-search-to-my-pelican-blog-with-datasette/).

## Getting Help

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/ryancheley/pelican-to-sqlite/issues)
- **Questions**: For general questions about usage, please open a [GitHub Discussion](https://github.com/ryancheley/pelican-to-sqlite/discussions)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](https://github.com/ryancheley/pelican-to-sqlite/blob/main/LICENSE) file for details.

## Author

Created by [Ryan Cheley](https://www.ryancheley.com)
