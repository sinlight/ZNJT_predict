#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:58:11 2017

@author: sinlight
"""
import pandas as pd
from datetime import datetime
from datetime import timedelta

tdata = pd.read_csv('~/pytest/cleand_df_withDateTime.csv',low_memory=False)
time_series = pd.read_csv('~/pytest/time_series_data.csv',low_memory=False)
time_series.index.name = 'start_time'

time_series.index = time_series.loc[:,'Unnamed: 0']

weekdata = tdata.loc[:,['start_time','link_ID']]

weekdata['wt1'] = 0
weekdata['wt2'] = 0
weekdata['wt3'] = 0
weekdata['wt4'] = 0
weekdata['wt5'] = 0
weekdata['wt6'] = 0
weekdata['wt7'] = 0
weekdata['wt8'] = 0
nullvalue = 0

for i in weekdata.index:
    dt = datetime.strptime( weekdata.loc[i,'start_time'], '%Y-%m-%d %H:%M:%S')
    
    dt1 = str(dt-timedelta(weeks=1))
    dt2 = str(dt-timedelta(weeks=2))
    dt3 = str(dt-timedelta(weeks=3))
    dt4 = str(dt-timedelta(weeks=4))
    dt5 = str(dt-timedelta(weeks=5))
    dt6 = str(dt-timedelta(weeks=6))
    dt7 = str(dt-timedelta(weeks=7))
    dt8 = str(dt-timedelta(weeks=8))
    try:
        weekdata.loc[i,'wt1']=time_series.loc[dt1,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt1']=999
    try:        
        weekdata.loc[i,'wt2']=time_series.loc[dt2,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt2']=999
    try:
        weekdata.loc[i,'wt3']=time_series.loc[dt3,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt3']=999
    try:
        weekdata.loc[i,'wt4']=time_series.loc[dt4,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt4']=999
    try:
        weekdata.loc[i,'wt5']=time_series.loc[dt5,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt5']=999
    try:
        weekdata.loc[i,'wt6']=time_series.loc[dt6,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt6']=999
    try:
        weekdata.loc[i,'wt7']=time_series.loc[dt7,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt7']=999
    try:
        weekdata.loc[i,'wt8']=time_series.loc[dt8,weekdata.loc[i,'link_ID']]
    except KeyError:
        weekdata.loc[i,'wt8']=999
    
weekdata.to_csv('~/pytest/weekdata.csv',encoding = 'utf_8')


















