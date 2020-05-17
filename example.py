from pyecharts.charts import Bar, Line, Kline, Map, ThemeRiver
from pyecharts.commons.utils import JsCode  # 高级绘图需要，默认不需要
from pyecharts import options as opts
import os
import json
import time
import requests
from flask import Flask
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from pyecharts.globals import ThemeType

from googletrans import Translator

# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))


app = Flask(__name__, static_folder="templates")


def get_chinaDayList():
    with open(os.path.join('data', 'data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        # 结果为list,{'date': '01.13', 'confirm': '41', 'suspect': '0', 'dead': '1', 'heal': '0'}
        chinaDayList = data['chinaDayList']
        # date = [x['date'] for x in chinaDayList]
        # confirm = [x['confirm'] for x in chinaDayList]
        # suspect = [x['suspect'] for x in chinaDayList]
        # dead = [x['dead'] for x in chinaDayList]
        # heal = [x['heal'] for x in chinaDayList]
        # chinadata = data['areaTree'][0]['children']     #全国数据，结果为列表
        worlddata = data['areaTree']
    return chinaDayList, worlddata
