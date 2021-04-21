#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2021/4/21
import os

from flask import Flask


def create_app(config=None):
    """
     create app 
    :param config: 
    :return: app
    """
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
    return app
