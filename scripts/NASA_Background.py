#!/usr/bin/env python
# coding: utf-8
import os
import re
import time
import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Error occurred'

date = time.strftime('%Y-%m-%d')
root = 'https://apod.nasa.gov/apod/'
web_date = int(date[2:].replace('-', '')) - 1
url = root + 'ap' + str(web_date) + '.html'


html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')
title = soup.title.string
name = title.split(' -')[1][:-1].replace(' ', '-')
file = 'NASA-' + date + name + '.jpg'

images = re.findall(r'image.+jpg', html)
image_url = root + images[0]

if not os.path.exists(file):
    try:
        requests.get(root, timeout=2)
    except:
        print('no network connection')

    r = requests.request('GET', image_url)
    r.raise_for_status()
    with open(file, 'wb') as f:
        f.write(r.content)
        f.close()
        print('Succesfully saved to %s'%file)
else:
    print('File already there')
