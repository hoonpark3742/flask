from cctv.data_reader import DataReader
import pandas as pd
import numpy as np

class CrimeRateModel:
    def __init__(self):
        self.dr = DataReader()

    def hook(self):
        self.create_crime_rate()

    def create_crime_rate(self):
            self.dr.context = './data/'
            self.dr.fname = 'saved/crime_police.csv'
            police_crime = self.dr.csv_to_dframe()
            print(police_crime.columns)
            print('---------- pivotal 전 ----------')

            # Index(['Unnamed: 0', '관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생',
            #        '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거', '구별'],
            #       dtype='object')

            police = pd.pivot_table(police_crime, index='구별', aggfunc=np.sum)
            print('----------  ----------')
            print('---------- pivotal 후 ----------')
            police['살인 검거율'] = police['살인 검거'] / police['살인 발생'] * 100
            police['강도 검거율'] = police['강도 검거'] / police['강도 발생'] * 100
            police['강간 검거율'] = police['강간 검거'] / police['강간 발생'] * 100
            police['절도 검거율'] = police['절도 검거'] / police['절도 발생'] * 100
            police['폭력 검거율'] = police['폭력 검거'] / police['폭력 발생'] * 100

            police.drop(columns={'살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거'}, axis=1)
            print(police.columns)
