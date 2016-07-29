Iget_lyrics
==========

這是一個簡單的腳本，用來下載歌詞  

* 主要用於命令行，默認輸出到終端，可以任意重定向。  
* 歌詞來源爲[蝦米網](http://www.xiami.com/)  
* 得到的不是歌詞文件，而是歌詞文本文件
* 腳本依賴與python2與模塊requests,lxml

使用方法：  
./get_lyrics.py `歌曲名`  
目前腳本還不是很完善，特殊情況幾乎沒有考慮，後續會陸續改進

getScores.py
===========
用來批量查看某一門課程的所有同學的成績,应该已经不再实用了，因为教务系统已经升级。

youdao.py  
========
用来在命令行使用有道网站查询单词。  
使用前安装python的requests以及lxml模块。  

```sh
pip install requests  
pip install lxml
```

使用方法:  

```sh
./youdao.py word
```

可以将其放到系统bin目录下以及使用alias简化使用。  

```sh
cp youdao.py /usr/bin
chmod +x /usr/bin/youdao.py
alias yd='youdao.py'
```

Add.py
========
把url添加到pocket（一个read it later应用）


