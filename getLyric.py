#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

from lxml import html
import requests
from lxml import etree
import sys

#BASE_URL="http://www.xiami.com/song/1769635405?spm=a1z1s.6843805.226669510.7.NIbDAF"
BASE_URL="http://www.xiami.com"
login_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}

def search(keyword):
    payload={'key':keyword}
    r=requests.get("http://xiami.com/search",params=payload,headers=login_header)

    doc = html.document_fromstring(r.text)
    song_td=doc.xpath(u"//td[@class='song_name']")
    if not len(song_td):
        return 0

    #get the right table
    if 1 == len(song_td[0]):
        return song_td[0][0].attrib['href']
    else:
        return song_td[0][1].attrib['href']

def get_lyr(lyric_url):
    r = requests.get(lyric_url,headers=login_header)
    doc = html.document_fromstring(r.text)

    ly_doc=doc.xpath(u"//div[@class='lrc_main']")
    if not ly_doc:
        print "这首歌在虾米上没有歌词！"
        return 0
    #use text_content() instead of text to get text without influence of <br>
    print ly_doc[0].text_content().strip()

if __name__=='__main__':
    lyr_url=search(sys.argv[1])
    if not lyr_url:
        print "Lyric can't be found from xiami!"
    else:
        get_lyr(lyr_url)

