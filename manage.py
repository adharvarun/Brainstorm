#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_list.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    # GitHub raw URL for the db.sqlite3 file
    db_url = "https://github.com/adharvarun/Brainstorm/raw/refs/heads/main/db.sqlite3"

    # Path where you want to save the database file locally
    db_path = "db.sqlite3"

    # Check if the file exists, if not, download it
    if not os.path.exists(db_path):
        print("Downloading the database from GitHub...")
        response = requests.get(db_url)
        with open(db_path, 'wb') as f:
            f.write(response.content)
        print("Database downloaded.")


if __name__ == '__main__':
    main()
