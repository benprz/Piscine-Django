#!/usr/bin/sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
django-admin startproject d05 && cd d05
python3 manage.py startapp ex00
