#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time : 2021/4/21

from website.app import App

app = App()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
