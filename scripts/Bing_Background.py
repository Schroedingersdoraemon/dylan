import re
import os
import json
import time
import requests

def getHTML(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Error occurred'


url = 'https://bing.biturl.top'
root = '/home/dylan/Pictures/BingWallpaper/'
date = time.strftime("%Y-%m-%d", time.localtime())
file = 'BingWallpaper-' + date + '.jpg'
files = os.listdir(root)
files.sort(reverse=True)
old_file = root + files[0]
os.system('feh --bg-fill %s'%old_file)
path = root + file

html = getHTML(url)
html_dict = json.loads(html)

start_date = html_dict['start_date']
end_date = html_dict['end_date']
pic_url = html_dict['url']
copyright = html_dict['copyright']

if not os.path.exists(path):
    if os.system('ping -q www.baidu.com -c 1'):
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

os.system('feh --bg-fill %s'%(path))
os.system("echo '%s' > /home/dylan/scripts/bing_copyright.txt\n"%copyright)

os.system('notify-send "%s"'%(copyright))
