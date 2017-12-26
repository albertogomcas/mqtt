import database
import sqlite3
from collections import defaultdict
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
import numpy as np
import pandas as pd

db = database.get_db()
df = pd.read_sql_query('select * from notifications;', db, parse_dates=['date'])
df.drop(columns=['id'], inplace=True)
df.payload = df.payload.astype('float')
df.set_index('date')

output_file("test.html")

p1 = figure(title='Temperature', x_axis_type="datetime")
p2 = figure(title='Humidity', x_axis_type="datetime", x_range=p1.x_range)

for topic, topicdf in df.groupby('topic'):
    print(topic)
    if 'dummy' in topic:
        continue
    if 'temperature' in topic:
        p1.line(topicdf.date, topicdf.payload, legend=topic)

    if 'humidity' in topic:
        p2.line(topicdf.date, topicdf.payload, legend=topic)

panel = gridplot([[p1, p2]])

p1.legend.location = "top_left"
p1.legend.click_policy = "hide"

p2.legend.location = "top_left"
p2.legend.click_policy = "hide"

show(panel)
