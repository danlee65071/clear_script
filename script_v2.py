#!/usr/bin/env python3
import re
import sys
import pip
import os

try:
    import pandas as pd
except:
    pip.main(['install', 'pandas'])
    import pandas as pd

csvs = [obj for obj in os.listdir() if obj[-4::] == '.csv']
os.mkdir('out_csv')
for csv_file in csvs:
    df = pd.read_csv('{}'.format(csv_file), sep=';')
    df.columns = ['text']
    df = df.drop_duplicates('text')
    regex_pat = re.compile(r'[^0-9-ёа-я ]', flags=re.IGNORECASE)
    df.text = df.text.str.replace(regex_pat,'')
    df.text = df.text.str.lower()
    df.text = df.text.str.replace('привет','').str.replace('помощник','').str.replace('пожалуйста','').\
    str.replace('алиса','').str.replace('ассистент','').str.replace('спасибо','').str.replace('товарищ','').str.replace('уже стенд','').str.replace('алло','').str.replace('здравствуйте','').str.replace('голосовой','').str.replace('сири','').str.replace('дорогой','').str.replace('робот','').str.replace('эй','').str.replace('добрый вечер','').str.replace('слушай','').str.replace('хэлоу','').str.replace('маруся','').str.replace('бот','')
    df.text = df.text.str.replace('салют','').str.replace('ок гугл','').\
    str.replace('афина','').str.replace('джой','').str.replace('спасибо','').str.replace('добрый день','')
    df.text = df.text.str.replace('  ',' ')
    df = df[df.text.str.len() < 80]
    df = df.drop_duplicates('text')
    name_csv = csv_file.replace('.csv', '')
    df.to_csv('out_csv/{}_out.csv'.format(name_csv), sep=';', index=False)
