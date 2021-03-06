#!/usr/bin/env python
import os
COV = None

if os.environ.get("FLASK_COVERAGE"):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

if os.path.exists('.env'):
    '''import env config'''
    print('Importing environment from .env ...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app, db
