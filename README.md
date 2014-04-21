get_lyrics
==========

get lyric text from http://www.xiami.com/ or  http://music.163.com/
這是一個簡單的腳本，用來下載歌詞  

* 主要用於命令行，默認輸出到終端，可以任意重定向。  
* 歌詞來源爲[蝦米網](http://www.xiami.com/)  
* 得到的不是歌詞文件，而是歌詞文本文件
* 腳本依賴與python2與requests模塊

使用方法：  
./get_lyrics `歌曲名`  
目前腳本還不是很完善，特殊情況幾乎沒有考慮，後續會陸續改進
