#!/usr/bin/env bash

git fetch origin && git reset --hard origin/master && git clean -f -d
python manage.py migrate