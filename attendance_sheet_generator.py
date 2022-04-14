#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pdfkit
import os

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
options = {
    "enable-local-file-access": True,
    'encoding': "windows-1254"
}

with open("courselist.html", 'rb') as html_doc:
    soup = BeautifulSoup(html_doc, 'lxml', from_encoding='windows-1254')

st_list = {}

for x in soup.find_all('tr'):
    if 'registered' in str(x):
        st_list[x.img.attrs['src1']] = {
            "img": "<img src=\"./../" + x.img.attrs['src'] + "\" width=\"75\" height=\"100\" border=\"0\">",
            "id": x.img.attrs['src1'],
            "name": x.contents[7].string,
            "surname": x.contents[9].string,
            "department": x.contents[17].string,
        }

df = pd.DataFrame.from_dict(st_list, orient='index')
df.columns = ['PICTURE', 'ID', 'NAME', 'SURNAME', 'DEPARTMENT']
df["SIGNATURE"] = ' '
df.index = np.arange(0, len(df))
df["ID"] = pd.to_numeric(df["ID"])

seating = pd.read_excel("seating.xlsx")
seating.columns = [i for i in range(0, 12)]

for column in range(0, 12):
    file_name = 'MT1'
    check = df.loc[df["ID"].isin(seating[column])]
    check.index = np.arange(0, len(check))
    if column <= 2:
        file_name += '_Session1'
    elif column <= 5:
        file_name += '_Session2'
    elif column <= 8:
        file_name += '_Session3'
    else:
        file_name += '_Session4'

    if column in [0, 3, 6, 9]:
        file_name += '_Class1'
    elif column in [1, 4, 7, 10]:
        file_name += '_Class2'
    elif column in [2, 5, 8, 11]:
        file_name += '_Class3'

    check.to_html("./MT1-Attendance/" + file_name + ".html", index=False, index_names=False, justify='center', escape=False, encoding='windows-1254')
    pdfkit.from_file("./MT1-Attendance/" + file_name + ".html", "./MT1-Attendance/" + file_name + ".pdf", configuration=config, options=options)
    os.remove("./MT1-Attendance/" + file_name + ".html")
    