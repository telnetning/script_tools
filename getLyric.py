#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from lxml import html
import requests
from lxml import etree

#BASE_URL="http://www.xiami.com/song/1769635405?spm=a1z1s.6843805.226669510.7.NIbDAF"
BASE_URL="http://www.xiami.com"
login_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}

def search(keyword):
    #s = requests.session()
    #search_key={'key':keyword}
    payload={'key':keyword}
    r=requests.get("http://xiami.com/search",params=payload,headers=login_header)
    #print r.url
    #r = s.get(BASE_URL,headers=login_header,data=search_key)
    doc = html.document_fromstring(r.text)
    #print etree.tostring(doc).encode('utf-8')
    song_td=doc.xpath(u"//td[@class='song_name']")
    #get the first table
    return song_td[0][0].attrib['href']

def get_lyr(lyric_url):
    r = requests.get(lyric_url,headers=login_header)
    doc = html.document_fromstring(r.text)
    #print etree.tostring(doc).encode('utf-8')
    ly_doc=doc.xpath(u"//div[@class='lrc_main']")
    #use text_content() instead of text to get text without influence of <br>
    print ly_doc[0].text_content().strip()

lyr_url=search('张三的歌')
get_lyr(lyr_url)

