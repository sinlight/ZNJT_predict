#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:46:16 2017

@author: sinlight
"""

import pandas as pd
data = pd.read_table('~/pytest/gy_contest_link_traveltime_training_data.txt',sep=';')
data = data.dropna(axis = 0)
time_intervals = []
start_times = []
end_times =[]
for i in data.index:
    time_interval = data.loc[i,'time_interval']
    time_interval = time_interval[1:-1]
    time_intervals.append(time_interval)
    time_split = time_interval.split(',')
    start_time = time_split[0]
    end_time = time_split[1]
    start_times.append(start_time)
    end_times.append(end_time)
    
data['time_interval1'] = time_intervals
data['start_time'] = start_times
data['end_time'] = end_times

data.to_csv('new_compete_data.csv',index = False,encoding = 'utf_8')



link_ID = data.loc[:,'link_ID']
link_ID = set(link_ID)
link_ID = list(link_ID)
link_ID.sort()


start_time = data['start_time']
start_time = list(set(start_time))
start_time.sort()


timedf = pd.DataFrame(0,index = start_time,columns = link_ID)

for i in data.index:
    stt = data.loc[i,'start_time']
    lid = data.loc[i,'link_ID']
    trt = data.loc[i,'travel_time']
    timedf.loc[stt,lid] = trt
    
timedf.to_csv('time_series_data.csv', encoding = 'utf_8')