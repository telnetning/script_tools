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


down\_android\_sourcer.sh  
==========
这个是我在按照官方文档下载Android源码的时候，由于某些并不太清楚的原因，下载过程会由于错误退出或者是类似于卡死的节奏，因此写了一个脚本，用来实现下面的功能  
*  每隔一分钟运行该脚本一次  
*  检查下载程序是否在运行，如果没有在运行，则运行  
*  如果下载程序正在运行，判断是否已经超过30分钟，如果是，判定为卡死，重新启动该下载程序   

脚本运行间隔时间和下载工作目录可以自定义。

extend\_vagrant\_commang.sh
======
这个是对vagrant命令的一点补充。  
由于vagrant的某些命令不具有全局性，常用的以下几个：  

+ vagrant ssh 
+ vagrang halt
+ vagrant suspend
+ vagrant up 
+ vagrant status

它们后面的参数一般是实例的name或者id，然而当是name的时候，这些命令不具有全局性了（这是因为name可能不唯一）。但是实际使用的时候，name常常会是不同的，这个时候vagrant的以上命令不能全局会导致不方便。  
所以有了这个小脚本，脚本只是对vagrant命令的一个补充，当以上的命令后面接的是实例的name的时候，我们的脚本会尝试对脚本的name（正确且唯一方可）进行解析，然后转换成id后进行命令执行。  
使用的时候将脚本里面的内容copy到`.bash_profile`中去，放入一个函数，并将vagrant命令指向这个函数即可。  
就像这样：  


```sh
alias vagrant=alias_vagrant

alias_vagrant () {
if [ $# -ne 2 ] || ([ $1 != "up" ] && [ $1 != "status" ] && [ $1 != "suspend" ] && [ $1 != "halt" ] && [ $1 !=  "ssh" ])
then
   for i in $@
       do
           /usr/bin/vagrant $*
   done
else
    id=`/usr/bin/vagrant global-status | grep $2 | awk '{print $1}'`
    if [ ${#id} -ne 7 ]
    then
        echo "请检查输入的name值是否正确且唯一"
    else
        /usr/bin/vagrant $1 $id
    fi
fi
}
```

getBingPic
====
这里命令用来获取 bing.com 的背景图片，bing.com 的图片很适合作为桌面背景图  
放在电脑上作为 crontab 任务每天跑一次即可。  

cron 示例：

+  确认 crond 打开
+  1 1 * * * /usr/bin/python2 /home/telnetning/crontabFold/getBingPic.py  #每天一点零一分运行
