#!/bin/bash
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app

# This script is used to run the Flask application with Gunicorn. on docker image