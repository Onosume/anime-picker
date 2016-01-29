# anime-picker

## What Is This?

This is an experimental website that picks what anime you should watch. The project is in development and cannot be run properly yet.

You'll be able to press a button on a webpage that will roll for a random anime. Don't like what you get? Roll again.

## How Does It Work?

anime-picker is built around the web framework Django.

## How Do I Get This To Work?

- Download Python 3.4.
- Install virtualenv using PyPI and then make and activate a virtualenv.
- Run `pip install -r requirements.txt` from the repository root.
    - This install pre-requisites like the correct version of Django.
- Create `animepicker/settings_local.py` based on `animepicker/settings.py`.
    - Replace the secret key with something appropriate when moving into production.
- Create a database and add the connection information into `animepicker/settings_local.py`.
    - For now this just uses sqlite. In production this should use the database engine that your web server supports.
    - In time I expect this to be upgraded to drop the database and move to use Hummingbird's API.
    - If you are using sqlite and are not me, you will not have a database file.
        - Run `python manage.py migrate`.
- At this point you should be able to create a superuser and access the admin panel.
- In the admin panel you can add different anime.
