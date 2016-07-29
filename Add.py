#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from lxml import html
from lxml import etree
import json
import re
import requests

login_param = {
        "feed_id":"your_account",
        "password":"your_pass",
        "form_check":"a7fa2faa41a24e35026f5b84ed601b3da1f5a27f0438e22cc77e9ec587fc35dd",
        "source":"email",
        "source_page":"/login",
        "is_ajax":"1",
}

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'}

item_act_url = "https://getpocket.com/a/x/itemAction.php"

if __name__ == '__main__':
    s = requests.Session()
    res = s.get("https://getpocket.com/login")

    doc = html.document_fromstring(res.text)
    form_check_list = doc.xpath(u"//input[@name='form_check']")
    form_check = form_check_list[0].get("value")
    login_param["form_check"] = form_check

    r = s.post("https://getpocket.com/login_process.php",  data=login_param)
    r2 = s.get("https://getpocket.com/a/queue/", headers = header)

    #尝试解析script标签
    r2_doc = html.document_fromstring(r2.text)
    script_list = r2_doc.xpath(u"//script")
    form_check_list = re.search(r"formCheck = \'([a-z0-9]*)\'", r2.text).group(1)

    res = s.post(item_act_url, data={"action":"add", "url":"http://example.com/", "formCheck":form_check_list}, headers=header)
    #print res.text
