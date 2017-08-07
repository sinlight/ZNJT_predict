#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:43:52 2017

@author: sinlight
"""
import pandas as pd
from datetime import datetime
from datetime import timedelta

tdata = pd.read_csv('~/pytest/cleand_df_withDateTime.csv',low_memory=False)
new_data = tdata.loc[:,['link_ID','length','width','pr_full']]
new_data = new_data.drop_duplicates()

firsttime = datetime.strptime('2016-06-01 08:00:00', '%Y-%m-%d %H:%M:%S')

time = firsttime

all_months = []
all_days = []
all_hours = []
all_minutes = []
all_hm_times = []
all_weekdays = []

all_times = []

for i in range(30):
    dtime = firsttime + timedelta(days=i)
    
    months = []
    days = []
    hours = []
    minutes = []
    hm_times = []
    weekdays = []
    
    times = []
    
    for j in range(30):
        time = dtime + timedelta(minutes=j*2)
        
        month = time.month
        day = time.day
        hour = time.hour
        minute = time.minute
        hm_time = time.time()
        weekday = time.weekday()
        
        months.append(month)
        days.append(day)
        hours.append(hour)
        minutes.append(minute)
        hm_times.append(hm_time)
        weekdays.append(weekday)
        times.append(time)
    
    all_months.extend(months)
    all_days.extend(days)
    all_hours.extend(hours)
    all_minutes.extend(minutes)
    all_hm_times.extend(hm_times)
    all_weekdays.extend(weekdays)
    all_times.extend(times)


d = {'start_time':all_times,'month':all_months,'day':all_days,'hour':all_hours,'minute':all_minutes,'time':all_hm_times,'weekday':all_weekdays}
time_frame = pd.DataFrame(d)

results = pd.DataFrame(columns=['link_ID','length','width','pr_full','start_time','month','day','hour','minute','time','weekday'])
#得到笛卡尔积
for i in new_data.index:
    result = time_frame.copy()
    result['link_ID'] = new_data.loc[i,'link_ID']
    result['length'] = new_data.loc[i,'length']
    result['width'] = new_data.loc[i,'width']
    result['pr_full'] = new_data.loc[i,'pr_full']
    
    results = results.append(result)
    
results.to_csv('x_predict.csv',index = False,encoding = 'utf_8') 