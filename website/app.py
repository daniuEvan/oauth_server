#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2021/4/21
import os

from flask import Flask


class App(object):
    def __init__(self, config=None):
        self.config = config
        self.app = Flask(__name__)

    def create_app(self):
        """ create app """
        # 加载默认配置
        self.app.config.from_object('website.settings')
        # 加载外部环境中的配置
        if 'WEBSITE_CONF' in os.environ:
            self.app.config.from_envvar('WEBSITE_CONF')
        # 加载用户指定设置
        if isinstance(self.config, dict):
            self.app.config.update(self.config)
        elif self.config.endswith('.py'):
            self.app.config.from_pyfile(self.config)
        return self.app

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)
