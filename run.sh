#!/bin/bash


# Checking environment, if it not found install virtualenv
cd ../
if ! [ -d ./venv/ ]; then
    if ! [ -f virtualenv.pyz ]; then
        wget https://bootstrap.pypa.io/virtualenv/3.6/virtualenv.pyz
    fi
    python3 virtualenv.pyz venv
fi
. venv/bin/activate
echo "Virtual environment successfully activated!"

# Export environ variables
if ! [ -f env.sh ]; then
    echo "WARNING! Environ variables failed to load!"
else
    . env.sh
    echo "Environ variables successfully exported!"
fi

# Back to root directory
cd public_html/

# Install dependencies
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver --settings='config.settings.prod'
