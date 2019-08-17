# Comics API
This repository represents an API for comic books, to be used as the backend for a comic book companion app.

## Dependencies
- Python 3.7
- Pipenv

To install pipenv

    comics_api# pip install pipenv

Install project dependencies

    comics_api$ pipenv install

Activate the Python environment

    comics_api$ pipenv shell

## Setting up the project

Copy `config-sample.py` to `config.py` and adjust the variables to your preferences. If you don't want to set up a database, uncomment the Sqlite section.

Create the database schema

    python create_tables.py

## Running the scraper

    scrapy runspider comics_scraper/comics_scraper/spiders/comixology.py

## Launching the webserver

    $ FLASK_APP=rest_api.py flask run

