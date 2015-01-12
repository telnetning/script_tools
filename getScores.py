#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from lxml import html 
import requests
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

BASE_URL = "http://210.27.12.1:90/queryDegreeScoreAction.do"
login_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}

def search(studentid,courseno):
    payload = {'degreecourseno':courseno,'studentid':studentid}
    r = requests.get(BASE_URL, params=payload, headers=login_header)
    #print r.url 
    doc = html.document_fromstring(r.text)
    person_info_lists = doc.xpath(u"//td")
    person_num = person_info_lists[0].text.split("：")
    print person_num[1].strip('\r\n '),
    person_name = person_info_lists[1].text.split("：")
    print "\t",
    print person_name[1].strip('\r\n '),

    score_info_lists = doc.xpath(u"//tr[@class='odd']/td")
    if score_info_lists:
        print "\t",
        if score_info_lists[3].text:
            print score_info_lists[3].text.strip('\r\n '),
            print "\t",
            print score_info_lists[4].text.strip('\r\n ')
        else:
            print "暂无成绩"
    else:
        print "暂无成绩"
if __name__ == '__main__':
    for i in range(2305,5355):
        studentid = '1407081717551062' + str(i) 
        search(studentid,"G00HA1010")
