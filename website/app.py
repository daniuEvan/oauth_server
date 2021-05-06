#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2021/4/21
import os
from flask import Flask
from website.models import db
from website.oauth2 import config_oauth
from website.routes import bp
from website.settings import DEBUGGER


def create_app(config=None):
    """
     create app 
    :param config: 
    :return: app
    """
    if DEBUGGER:
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app = Flask(__name__)
    # 加载默认配置
    app.config.from_object('website.settings')
    # 加载外部环境中的配置
    if 'WEBSITE_CONF' in os.environ:
        app.config.from_envvar('WEBSITE_CONF')
    # 加载用户指定设置
    if isinstance(config, dict):
        app.config.update(config)
    elif config.endswith('.py'):
        app.config.from_pyfile(config)
    # 初始化app
    setup_app(app)
    return app


def setup_app(app):
    # 表不存在先创建
    @app.before_first_request
    def create_tables():
        db.create_all()

    db.init_app(app)
    config_oauth(app)
    app.register_blueprint(bp, url_prefix='')
