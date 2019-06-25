"""Module captures and formats the data provided by Baltimore Corps on fellowship use throughout the City. Provides a data variable to make the information available as an import to other modules in project for analysis. 
Created 6-22-2019  by Babila R. Lima
"""

import numpy as np
import pandas as pd

agency = ["Mayor's Office","Mayor's Office",'MOED','MOED','BCHD','BCHD','BCHD','BCHD',
          'BCHD','BCHD','BCHD','BCHD','BCHD','BCHD','BCHD','MOED','BPD',
          'City Hall: Z.Cohen','BCPS','Human Services','BCHD','BCHD','BCHD','BCHD',
          'BCHD','BCHD','BCHD','BCPS','City Hall: Z.Cohen','City Hall: Z.Cohen','DGS',
          'BCF','MOCJ','MOED','MOED','MOED','MOED','DGS','DGS','DGS','BBMR','BBMR',
          'BCHD','BCHD','BCHD','BCHD','BCHD','MOCJ','MIMA','City Hall: Z.Cohen','BCF','BCHD']

funding = ['BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE',
           'BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE','Grant Funded','Grant Funded',
           'BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE','Grant Funded','Grant Funded',
           'Grant Funded','BoE','Grant Funded','BoE','Grant Funded','Grant Funded',
           'Grant Funded','Grant Funded','BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE',
           'BoE','BoE','Family Leauge','BoE','Grant Funded','BCF','BoE' ]

program = ['Fellowship','Fellowship','Fellowship','Fellowship','Fellowship','Fellowship',
           'Fellowship','Fellowship','Fellowship','Fellowship','Fellowship','Fellowship',
           'Fellowship','Fellowship','Fellowship','Fellowship','Fellowship','Fellowship',
           'Place4Purpose','Fellowship','Fellowship','Fellowship','Fellowship','Fellowship',
           'Fellowship','Fellowship','Fellowship','Fellowship','Fellowship','Fellowship',
           'Fellowship','Place4Purpose','Place4Purpose','Place4Purpose','Place4Purpose',
           'Fellowship','Fellowship','Fellowship','Fellowship','Fellowship','Fellowship',
           'Fellowship','Fellowship','Fellowship','Fellowship','Fellowship','Fellowship',
           'Place4Purpose','Place4Purpose','Place4Purpose','Place4Purpose','Place4Purpose']

year = [2014,2014,2015,2015,2015,2015,2015,2015,2015,2015,2016,2016,2016,2016,2016,2016,
        2016,2016,2016,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,
        2017,2017,2017,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,
        2018,2018,2018,2018]

datetime_year = pd.to_datetime(year, format='%Y')
dframe = pd.DataFrame(agency, index=datetime_year, columns=['agency'])
dframe['year'] = dframe.index.year
dframe['funding'] = funding
dframe['program'] = program

avg_stipend =  (np.where(dframe.index == pd.to_datetime('2014'),32000,
                np.where(dframe.index == pd.to_datetime('2015'),33000,
                np.where((dframe.index == pd.to_datetime('2016')) & (dframe['program'] == 'Fellowship'),38112.50,
                np.where((dframe.index == pd.to_datetime('2016')) & (dframe['program'] == 'Place4Purpose'),60000,
                np.where((dframe.index == pd.to_datetime('2017')) & (dframe['program'] == 'Fellowship'),40465.33,
                np.where((dframe.index == pd.to_datetime('2017')) & (dframe['program'] == 'Place4Purpose'),38750,
                np.where((dframe.index == pd.to_datetime('2018')) & (dframe['program'] == 'Fellowship'),39666.67,
                np.where((dframe.index == pd.to_datetime('2018')) & (dframe['program'] == 'Place4Purpose'),64600,None)))))))))

## use average stipend for each program for the fellow stipend ## 
dframe['stipend'] = avg_stipend
dframe['fringe'] = dframe['stipend'] * .22
dframe['unemployment'] = 1000
dframe['BaltCorps_fee'] = 2000
dframe['StrongCity_fee'] = 2000
dframe['fellow_cost'] = (dframe['stipend'] + dframe['fringe'] + dframe['unemployment'] + 
                         dframe['BaltCorps_fee'] + dframe['StrongCity_fee'])

dframe['fellows_count'] = dframe.groupby([dframe.index, 'agency'])['agency'].transform('count')
dframe['annual_spending_by_agency'] = dframe.groupby([dframe.index, dframe['agency']])['fellow_cost'].transform('sum')

dframe = dframe[dframe['agency'] != 'BCPS'] # remove school system 
