pgbackup
========

CLI for backup remote PostgreSQL database either locall or to s3

Preparing the development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository
3. ``cd`` into the repository
4. Fetch development dependencies ``make install``
5. Activate virtualnenv:  ``pipenv shell``


Usage
-----

Pass in a full database URL, the storage driver, and the destination

s3 Example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/deb_one/backups/dump.sql



Running Test
------------

Run tests locally using ``make`` if virtualenv is actiave:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make


