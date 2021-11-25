import tkinter as tk
from tkinter.filedialog import *
import re
import pip
import os

try:
    import pandas as pd
except:
    pip.main(['install', 'pandas'])
    import pandas as pd


def process_csv(csvs):
    try:
        os.mkdir('out_csv')
    except OSError:
        pass
    for csv_file in csvs:
        df = pd.read_csv('{}'.format(csv_file), sep=';')
        df.columns = ['text']
        df = df.drop_duplicates('text')
        regex_pat = re.compile(r'[^0-9-ёа-я ]', flags=re.IGNORECASE)
        df.text = df.text.str.replace(regex_pat, '')
        df.text = df.text.str.lower()
        df.text = df.text.str.replace('привет', '').str.replace('помощник', '').str.replace('пожалуйста', ''). \
            str.replace('алиса', '').str.replace('ассистент', '').str.replace('спасибо', '').str.replace('товарищ',
                                                                                                         '').str.replace(
            'уже стенд', '').str.replace('алло', '').str.replace('здравствуйте', '').str.replace('голосовой',
                                                                                                 '').str.replace('сири',
                                                                                                                 '').str.replace(
            'дорогой', '').str.replace('робот', '').str.replace('эй', '').str.replace('добрый вечер', '').str.replace(
            'слушай', '').str.replace('хэлоу', '').str.replace('маруся', '').str.replace('бот', '')
        df.text = df.text.str.replace('салют', '').str.replace('ок гугл', ''). \
            str.replace('афина', '').str.replace('джой', '').str.replace('спасибо', '').str.replace('добрый день', '')
        df.text = df.text.str.replace('  ', ' ')
        df = df[df.text.str.len() < 80]
        df = df.drop_duplicates('text')
        name_csv = csv_file.split('/')[-1].replace('.csv', '')
        df.to_csv('out_csv/{}_out.csv'.format(name_csv), sep=';', index=False)


def get_csv_name():
    of = askopenfilenames()
    csvs = [obj for obj in of if obj[-4::] == '.csv']
    process_csv(csvs)


window = tk.Tk()
window.title('clear_csv')
window.geometry('300x300')
window.minsize(300, 300)
window.maxsize(300, 300)

frame_add_csv = tk.Frame(window, width=300, height=300)
btn_add_csv = tk.Button(window, text='Добавить csv', bg='green', fg="#ccc", padx="20", pady="8", font="16",
                        command=lambda: get_csv_name())

frame_add_csv.place(relx=0, rely=0, relwidth=1, relheight=1)
btn_add_csv.pack()

window.mainloop()
