# Creating the tables
You will need to install Postgres or Sqlite. Sqlite should come with Python automatically, so if you're feeling lazy, just use that. Keep in mind I have not tested Sqlite at all.
To create the tables for the database:
1. Make a copy of config-sample.py and rename it to config.py.
2. Edit config.py by uncommenting the database you wish to use. Choose only one.
3. Run the following command

	python -i -c "from comics_api.utils import *; comixology_setup();"

# Rebuilding the tables
If you get an error such as this

	Traceback (most recent call last):
	  File "/home/edc/.virtualenvs/comics_api-ZmkYeqLQ/lib/python3.7/site-packages/peewee.py", line 2981, in execute_sql
		cursor.execute(sql, params or ())
	psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "creator_pkey"
	DETAIL:  Key (url)=(https://www.comixology.com/Various/comics-creator/1368) already exists.
	
Then the tables already exist. Ask yourself: Did you mean to run this again? If you did, then you must first delete the existing tables.

Drop all the tables created from the above script manually, then re-run the python command. Use a SQL interface like PgAdmin, browse for the table names, and run

	drop table if exists ref_creator_role cascade;
	drop table if exists creator cascade;
	drop table if exists issue cascade;
	drop table if exists publisher cascade;
	drop table if exists j_issue_creator cascade;
	drop table if exists ref_age_rating cascade;
	drop table if exists ref_sold_by cascade;
	drop table if exists series cascade;
	drop table if exists volume cascade;
	drop table if exists story_arc cascade;
	drop table if exists genre cascade;
	drop table if exists volume cascade;
	
The table names may not be accurate.


# Running the scraper

	scrapy runspider comics_api/scraper/spiders/comixology.py
