#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   finish.py    
@Contact :   xxx130032@gmail.com
@Author  :   Meteor
@Modify Time      @Version    @Desciption
------------      --------    -----------
2025/7/14 16:03    1.0         None
"""
from pyecharts.charts import Page

Page.save_resize_html(
    source="./template/test.html",
    cfg_file="./template/chart_config.json",
    dest="./template/deshboard.html",
)
