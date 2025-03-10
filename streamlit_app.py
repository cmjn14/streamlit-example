from collections import namedtuple
from streamlit_echarts import st_echarts
import altair as alt
# import drawsvg as dw
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# Calcul distances et angle à partir des coordonnées : https://www.movable-type.co.uk/scripts/latlong.html
# Python GEDCOM parser : https://pypi.org/project/python-gedcom/

# initial angle between sosa 2 and 3 (generation 2), in degrees
theta2 = 24
final_year = 2000

def get_generation(sosa):
    # sosa 1 = generation 1
    generation = int(math.log(sosa,2)) + 1
    return generation

def get_order_in_generation(sosa):
    # order starting at 0 for each generation
    # used to determine angle in the graph
    generation = get_generation(sosa)
    order = sosa - (2 ** (generation - 1))
    order
    return order

def get_angle(sosa):
    st.write("---")
    st.write("sosa ", sosa)
    generation = get_generation(sosa)
    number_in_generation = 2 ** (generation - 1)
    if sosa > 1:
        theta_span = theta2 * (2 ** (generation - 1) - 1) / (generation - 1) # ??? must be false
        theta_start = theta_span * -0.5
        theta_delta = theta_span / (number_in_generation - 1)
        order = get_order_in_generation(sosa)
        theta_sosa = theta_start + theta_delta * order
        st.write("result: ", theta_sosa)
        return theta_sosa
    else:
        return 0
    # thota_sosa in degrees
    
get_angle(2)
get_angle(3)
get_angle(4)
get_angle(5)
get_angle(6)
get_angle(7)
get_angle(8)
get_angle(15)
get_angle(64)
get_angle(127)
get_angle(128)
get_angle(256)

                 
                     
def render_scatter():
    hours = ['12a', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a','10a','11a','12p', '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', '11p']
    days = ['Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday', 'Sunday']
    data = [[0,0,5],[0,1,1],[0,2,0],[0,3,0],[0,4,0],[0,5,0],[0,6,0],[0,7,0],[0,8,0],[0,9,0],[0,10,0],[0,11,2],[0,12,4],[0,13,1],[0,14,1],[0,15,3],[0,16,4],[0,17,6],[0,18,4],[0,19,4],[0,20,3],[0,21,3],[0,22,2],[0,23,5],[1,0,7],[1,1,0],[1,2,0],[1,3,0],[1,4,0],[1,5,0],[1,6,0],[1,7,0],[1,8,0],[1,9,0],[1,10,5],[1,11,2],[1,12,2],[1,13,6],[1,14,9],[1,15,11],[1,16,6],[1,17,7],[1,18,8],[1,19,12],[1,20,5],[1,21,5],[1,22,7],[1,23,2],[2,0,1],[2,1,1],[2,2,0],[2,3,0],[2,4,0],[2,5,0],[2,6,0],[2,7,0],[2,8,0],[2,9,0],[2,10,3],[2,11,2],[2,12,1],[2,13,9],[2,14,8],[2,15,10],[2,16,6],[2,17,5],[2,18,5],[2,19,5],[2,20,7],[2,21,4],[2,22,2],[2,23,4],[3,0,7],[3,1,3],[3,2,0],[3,3,0],[3,4,0],[3,5,0],[3,6,0],[3,7,0],[3,8,1],[3,9,0],[3,10,5],[3,11,4],[3,12,7],[3,13,14],[3,14,13],[3,15,12],[3,16,9],[3,17,5],[3,18,5],[3,19,10],[3,20,6],[3,21,4],[3,22,4],[3,23,1],[4,0,1],[4,1,3],[4,2,0],[4,3,0],[4,4,0],[4,5,1],[4,6,0],[4,7,0],[4,8,0],[4,9,2],[4,10,4],[4,11,4],[4,12,2],[4,13,4],[4,14,4],[4,15,14],[4,16,12],[4,17,1],[4,18,8],[4,19,5],[4,20,3],[4,21,7],[4,22,3],[4,23,0],[5,0,2],[5,1,1],[5,2,0],[5,3,3],[5,4,0],[5,5,0],[5,6,0],[5,7,0],[5,8,2],[5,9,0],[5,10,4],[5,11,1],[5,12,5],[5,13,10],[5,14,5],[5,15,7],[5,16,11],[5,17,6],[5,18,0],[5,19,5],[5,20,3],[5,21,4],[5,22,2],[5,23,0],[6,0,1],[6,1,0],[6,2,0],[6,3,0],[6,4,0],[6,5,0],[6,6,0],[6,7,0],[6,8,0],[6,9,0],[6,10,1],[6,11,0],[6,12,2],[6,13,1],[6,14,3],[6,15,4],[6,16,0],[6,17,0],[6,18,0],[6,19,0],[6,20,1],[6,21,2],[6,22,2],[6,23,6]]
    data1 = [
        {"sosa": 2, "first": "Cédric", "last": "Lopez", "birth": {"year": 1973, "place": "Evreux"}} 
    ]
            
    options = {
        "title": {
            "text": "Punch Card of Github",
            "link": "https://github.com/pissang/echarts-next/graphs/punch-card"
        },
        "legend": {
            "data": ["Punch Card"],
            "left": "right"
        },
        "polar": {},
        "tooltip": {
            "formatter": "{value}%"
        },
        "angleAxis": {
            "type": "category",
            "data": hours,
            "boundaryGap": False,
            "splitLine": {
                "show": False,
                "lineStyle": {
                    "color": "#999",
                    "type": "dashed"
                }
            },
            "axisLine": {
                "show": False
            }
        },
        "radiusAxis": {
            "type": "value",
            "min": 1700,
            "max": final_year,
            "inverse": True,
            "axisLine": {
                "show": True
            },
            "axisLabel": {
                "rotate": 0
            }
        },
        "series": [{
            "name": "Punch Card",
            "type": "scatter",
            "coordinateSystem": "polar",
            "symbolSize": "{value[2]}%",
            "data": data,
            "animationDelay": 0
        }]
    }
    st_echarts(
        options=options, height="800px",
    )

render_scatter()

def render_pie_simple():
    options = {
        "title": {"text": "某站点用户访问来源", "subtext": "纯属虚构", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {"orient": "vertical", "left": "left",},
        "series": [
            {
                "name": "访问来源",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1048, "name": "搜索引擎"},
                    {"value": 735, "name": "直接访问"},
                    {"value": 580, "name": "邮件营销"},
                    {"value": 484, "name": "联盟广告"},
                    {"value": 300, "name": "视频广告"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    st_echarts(
        options=options, height="600px",
    )

render_pie_simple()

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

