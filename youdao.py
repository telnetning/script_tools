#!/usr/bin/env python

import sys
import requests
from lxml import html
from lxml import etree

BASE_URL = "http://dict.youdao.com/search"
URL_HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}

def translate(word):
    payload = {'q':word}
    r = requests.get(BASE_URL, params=payload, headers=URL_HEADER)

    doc = html.document_fromstring(r.text)
    tran_li = doc.xpath(u"//div[@id='phrsListTab']/div[@class='trans-container']/ul/li")
    for piece in tran_li:
        print piece.text

if __name__ == '__main__':
    word = sys.argv[1]
    if not word:
        print "usage: youdao.py word"
    else:
        translate(word)
