#!/bin/bash

# Activate the virtual environment (if applicable)
# source /path/to/your/venv/bin/activate

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Set execution permissions for the script
chmod +x build_files.sh
