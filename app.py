#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2021/4/21
from website.app import create_app

# flask app
app = create_app(config={
    'SECRET_KEY': 'secret',
    'OAUTH2_REFRESH_TOKEN_GENERATOR': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
