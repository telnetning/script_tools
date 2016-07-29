#/usr/bin/env bash

#by telnenting
#2013年 11月 12日 星期二 20:21:11 CST
#为了解决下载Android源码过程中，由于网络问题，进程经常会自动退出或者假死状态
#脚本自动处理，每一分钟运行一次
#如果没有下载进程，则新建，若进程已经持续超过半小时，判定为进程卡死，重新启动

#程序睡眠时间
SlEEPTIME=60
workspace="/home/telnetning/workspace"
#函数用来启动进程
start_pro()
{
    cd $workspace
    repo sync
}

#主要函数
main_process()
{
    #得到软件运行实例的PID
    process_id=`ps aux | grep repo | grep python | awk '{print $2}'`

    if [ -z $process_id ]
    then
	    start_pro
    else
        #得到该进程已经运行的时间，若大于某一个时间值，将kill掉它并重新启动
	    last_time=`ps -eo pid,etime | grep $process_id | awk '{print $2}' | awk -F ":" '{print $1}'`
	    if [ "$last_time>30" ]
	    then
	    	kill -9 $process_id
		    start_pro
        fi
    fi
}

#每隔一分钟运行一次该程序
while true ;do
{
    main_process
    sleep $SLEEPTIME
}	
done
