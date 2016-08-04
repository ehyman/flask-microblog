#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__name__))

# login configuration
CSRF_ENABLED = True
SECRET_KEY = "P\x88\xe5\xc1-\x01QD3\xeb\x81@"
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
]

# database configuration
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')