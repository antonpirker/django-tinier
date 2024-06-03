#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from pathlib import Path


# BASE_DIR = parent of manage.py file
BASE_DIR = Path(__file__).resolve().parent 

# NOTE: This line will let Django handle models in the root folder
sys.path.append(str(BASE_DIR.parent))


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
