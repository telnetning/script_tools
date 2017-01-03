#!/usr/bin/python2
# -*- coding: utf-8 -*-

from lxml import html
import requests
import sys
import re

BASE_URL = "http://www.bing.com"
HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}
PICDIC = "/home/telnetning/Pictures/wallpaperFromBing/"
def downloadImageFile(imgUrl):  
    local_filename = imgUrl.split('/')[-1]  
    #print "Download Image File=", local_filename  
    r = requests.get(imgUrl, stream=True) # here we need to set stream = True parameter  
    with open(PICDIC + local_filename, 'wb') as f:  
        for chunk in r.iter_content(chunk_size=1024):  
            if chunk: # filter out keep-alive new chunks  
                f.write(chunk)  
                f.flush()  
        f.close()  
    return local_filename  

def getPicURL():
    r = requests.get(BASE_URL, headers = HEADER)
    pic_path = re.search(r'g_img=\{url:\ \"([\w/_-]+.jpg)\"', r.text).group(1)
    #print pic_path
    return BASE_URL + pic_path 

if __name__ == '__main__':
    reload(sys)                      # reload 才能调用 setdefaultencoding 方法  
    sys.setdefaultencoding('utf-8')  # 设置 'utf-8' 
    downloadImageFile(getPicURL()) 
