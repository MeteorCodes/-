#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   charts.py
@Contact :   xxx130032@gmail.com
@Author  :   Meteor
@Modify Time      @Version    @Desciption
------------      --------    -----------
2025/7/13 17:13    1.0         None
"""
from screeninfo import get_monitors
from pyecharts import options as opts
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
from pyecharts.charts import Page, Pie, Map, Bar, Line, Polar
from pyecharts.globals import CurrentConfig
import csv

CurrentConfig.ONLINE_HOST = "static/js/"

# 获取所有显示器的信息
monitor = get_monitors()[0]
mw, mh = monitor.width, monitor.height

page = Page(
    layout=Page.DraggablePageLayout,
    page_title="中国人口数据",
    # page_border_color="#D3D3D3"
)
# 大标题
table_1 = Table()
header = ["中国人口时钟可视化大屏"]
table_1.add(header, rows=[], attributes={
    "align": "center",
})
table_1.set_global_opts()
page.add(table_1)

# 饼图
with open("./data/population_clock_data.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    man_sj = rows[1]["栏目"][9:-2]
    woman_sj = rows[2]["栏目"][8:-2]

pie = (
    Pie(init_opts=opts.InitOpts(width=f"{mw / 8.53}px", height=f"{mh / 8}px"))
    .add("", [("男", man_sj), ("女", woman_sj)])
    .set_global_opts(title_opts=opts.TitleOpts(title="男女比例"))
)
page.add(pie)

# 地图
with open("./data/hongheiku_data.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

data = []
for row in rows[1:]:
    data.append((row["地区"], row["人口数"]))

map = (
    Map(init_opts=opts.InitOpts(width=f"{mw / 2.56}px", height=f"{mh / 2}px"))
    .add("人口", data, maptype="china", zoom=1.2)
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=rows[1]["人口数"]),
        title_opts=opts.TitleOpts(title="人口分布")
    )
)
page.add(map)

# 宗教数据
with open("./data/religion_table.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

religion = []
num = []
percentage = []
for row in rows:
    religion.append(row["宗教"])
    num.append(row["粉丝数量"].replace(" ", ""))
    percentage.append(row["总人口百分比"].replace(" %", ""))

bar = (
    Bar(init_opts=opts.InitOpts(width=f"{mw / 5.12}px", height=f"{mh / 4}px"))
    .add_xaxis(religion)
    .add_yaxis("粉丝数量", num, bar_width="50%")
    .add_yaxis("总人口百分比", percentage)
    .set_global_opts(title_opts=opts.TitleOpts(title="宗教数据"),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45, interval=0)), )
)
page.add(bar)

# 折线图
with open("./data/population_histort.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
year = []
population = []
growth = []
for row in rows:
    year.append(row["年份"])
    population.append(row["人口"].replace(" ", ""))
    growth.append(row["成长率"].replace(" %", ""))

line = (
    Line(init_opts=opts.InitOpts(width=f"{mw / 1.28}px", height=f"{mh / 6}px"))
    .add_xaxis(year)
    .add_yaxis("人口", population, is_smooth=True)
    .add_yaxis("成长率", growth, is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="中国人口史"))
)
page.add(line)

# 人口预测
with open("./data/population_forecast_histort.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

year = []
population = []
growth = []
for row in rows:
    year.append(row["年份"])
    population.append(row["人口"].replace(" ", ""))
    growth.append(row["成长率"].replace(" %", ""))

polar = (
    Polar(init_opts=opts.InitOpts(width=f"{mw / 6}px", height=f"{mh / 4}px"))
    .add_schema(radiusaxis_opts=opts.RadiusAxisOpts(data=year, type_="category"))
    .add("人口", population, type_='bar')
    .add("成长率", growth, type_='bar')
    .set_global_opts(title_opts=opts.TitleOpts(title="人口预测"))
)
page.add(polar)

page.render("./template/test.html")
