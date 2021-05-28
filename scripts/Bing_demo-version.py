#!/usr/bin/env python
# coding: utf-8

# In[150]:


import re
import os
import json
import time
import requests


# In[151]:


def getHTML(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Error occurred'


# In[152]:


url = 'https://bing.biturl.top'
root = '/home/dylan/Pictures/BingWallpaper/'
date = time.strftime("%Y-%m-%d", time.localtime())
file = 'BingWallpaper-' + date + '.jpg'
old_file = root + os.listdir('/home/dylan/Pictures/BingWallpaper')[0]
os.system('feh --bg-fill %s'%old_file)
path = root + file

html = getHTML(url)
html_dict = json.loads(html)


# In[153]:


start_date = html_dict['start_date']
end_date = html_dict['end_date']
pic_url = html_dict['url']
copyright = html_dict['copyright']


# In[154]:


if not os.path.exists(path):
    if os.system('ping www.baidu.com -c 1'):
        file = os.listdir('~/Pictures/BingWallpaper')[0]
        path = root + file
    else:
        r = requests.request('GET', pic_url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('Successfully saved to %s'%path)
else:
    print('File already there')


# In[136]:


os.system('feh --bg-fill %s'%(path))


# In[137]:


os.system('notify-send "%s"'%(copyright))


import requests, os, parsel, time, sys, ctypes, subprocess

def changePaper(img_path):
    # 设置壁纸
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
    command = 'reg add \"hkcu\\control panel\\desktop\" /v \"wallpaper\" /d \"' + img_path + '\" /f'
    subprocess.run(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    '''
    刷新
    'RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters'
    '''

def isConnected():
    # 测试是否有网
    try:
        requests.get("https://cn.bing.com", timeout=2)
    except:
        return False
    return True

Date = time.strftime("%Y-%m-%d", time.localtime())
MainPath = os.path.dirname(os.path.realpath(sys.argv[0])) + '\\Wallpapers'
paperPath = MainPath + '\\' + Date + '必应壁纸.jpg'

def getPaper():
    # 下载壁纸
    try:
        link = 'https://cn.bing.com'
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        response_str = requests.get(link, headers).text
        html = parsel.Selector(response_str)
        li = html.xpath('//link[@id="bgLink"]/@href').get()
        url = link + li
        img_data = requests.get(url, headers=headers).content
        with open(paperPath, 'wb') as f:
            f.write(img_data)
    except :
        pass

if os.path.exists(paperPath):
    changePaper(paperPath)
else:
    if not os.path.exists(MainPath):
        os.makedirs(MainPath)
    for i in range(100):
        if isConnected():
            getPaper()
            changePaper(paperPath)
            break
        time.sleep(3)
