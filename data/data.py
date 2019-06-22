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
          'BCHD','BCHD','BCHD','BCHD','BCHD','MOCJ','MIMA','City Hall: Z.Cohen','BCF']

funding = ['Contractual','Contractual','BoE','BoE','BoE','BoE','BoE','BoE','BoE',
           'BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE','Grant Funded','Grant Funded',
           'BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE','Grant Funded','Grant Funded',
           'Grant Funded','BoE','Grant Funded','BoE','Grant Funded','Grant Funded',
           'Grant Funded','Grant Funded','BoE','BoE','BoE','BoE','BoE','BoE','BoE','BoE',
           'BoE','BoE','Family Leauge','BoE','Grant Funded','BCF' ]

year = [2014,2014,2015,2015,2015,2015,2015,2015,2015,2015,2016,2016,2016,2016,2016,2016,
        2016,2016,2016,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,
        2017,2017,2017,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,
        2018,2018,2018]

datetime_year = pd.to_datetime(year, format='%Y')

dframe = pd.DataFrame(agency, index=datetime_year, columns=['agency'])
dframe['funding'] = funding
dframe['avg_stipend'] = 44000
dframe['fringe'] = dframe['avg_stipend'] * .22
dframe['unemployment'] = 1000
dframe['BaltCorps_fee'] = 2000
dframe['StrongCity_fee'] = 2000
dframe['fellow_cost'] = (dframe['avg_stipend'] + dframe['fringe'] + dframe['unemployment'] + 
                         dframe['BaltCorps_fee'] + dframe['StrongCity_fee'])



