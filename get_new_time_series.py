#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:13:51 2017

@author: sinlight
"""

import pandas as pd
from datetime import datetime

time_series = pd.read_csv('~/pytest/time_series_data.csv',low_memory=False)

months = []
days = []
hours = []
minutes = []
times = []
weekdays = []

for i in time_series.index:
    id1series=time_series.loc[:,'Unnamed: 0']
    timeTuple = datetime.strptime( id1series[i], '%Y-%m-%d %H:%M:%S')
    
    #增加时间选项
    month = timeTuple.month
    day = timeTuple.day
    hour = timeTuple.hour
    minute = timeTuple.minute
    time = timeTuple.time()
    weekday = timeTuple.weekday()
    months.append(month)
    days.append(day)
    hours.append(hour)
    minutes.append(minute)
    times.append(time)
    weekdays.append(weekday)
    
time_series['month'] = months
time_series['day'] = days
time_series['weekday'] = weekdays
time_series['hour'] = hours
time_series['minute'] = minutes
time_series['time'] = times

time_series.to_csv('new_time_series.csv',index=False,encoding = 'utf_8')