#!/bin/bash
# USE FROM: ../public_html/

# Install virtualenv and activate it
cd ../
if ! [ -d ./django/ ]; then
    if ! [ -f virtualenv.pyz ]; then
        wget https://bootstrap.pypa.io/virtualenv/3.6/virtualenv.pyz
    fi
    python3 virtualenv.pyz django
fi
. django/bin/activate
echo "Virtual environment successfully activated!"

# Export variables to environment
if [ -f env.sh ]; then
    . env.sh
    echo "Environ variables successfully exported!"
else
    echo "WARNING! Environ variables failed to load!"
fi

# Install dependencies
cd public_html/
pip install -r requirements.txt

# Deploy website, activate database and run server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver --settings='config.settings.prod'
