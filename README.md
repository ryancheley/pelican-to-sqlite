# pelican-to-sqlite

Create a SQLite database containing data posts from your local [pelican](https://blog.getpelican.com) markdown files

## How to install

    $ pip install pelican-to-sqlite

## Usage

Once the plugin has been installed you only need to run `'make html` to create a SQLite database called `pelican.db` which will be created in the root of your pelican site. 

You will need to add a form to your `base.html` template (or similar template depending on your theme). The form that needs to be added looks like this (assuming you use [Tailwind](https://tailwindcss.com)):

```
    <section class="relative h-8">
    <section class="absolute inset-y-0 right-10 w-128">
    <form
    class = "pl-4"
    <
    action="your-action-link-here"
    method="get">
            <label for="site-search">Search the site:</label>
            <input type="search" id="site-search" name="text"
                    aria-label="Search through site content">
            <button class="rounded-full w-16 hover:bg-blue-300">Search</button>
    </form>
    </section>
```

In the above, `your-action-link-here` should be substituted for the link that you get from your Vercel hosted instance of `datasette`.

## Deploy using Vercel

There are many options to deploy your SQLite database with `datasette`. Below describes using Vercel.

First, install `datasette` using pip

```
    pip install datasette
```

Next, install the datasette plugin `datasette-publish-vercel` using pip

```
    pip install datasette-publish-vercel
```

and the [Vercel CLI](https://vercel.com/cli)

Once that's done, run `vercel login` to login to (or create) an account.

To publish your `pelican.db` to Vercel just run:

```
    datasette publish vercel my-database.db
```

There are several options for outputting to Vercel. See the [documentation](https://github.com/simonw/datasette-publish-vercel/blob/main/README.md) for more details

## Using with Datasette

The SQLite database produced by this tool is designed to be browsed using [Datasette](https://datasette.readthedocs.io/). See my post [Adding Search to My Pelican Blog with Datasette](https://www.ryancheley.com/2022/01/16/adding-search-to-my-pelican-blog-with-datasette/) for more details. 
