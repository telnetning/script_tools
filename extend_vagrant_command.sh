#!/usr/bin/env bash

if [ $# -ne 2 ] || ([ $1 != "up" ] && [ $1 != "status" ] && [ $1 != "suspend" ] && [ $1 != "halt" ] && [ $1 !=  "ssh" ])
then
   for i in $@
       do
           /usr/bin/vagrant $*
   done
else
    id=`/usr/bin/vagrant global-status | grep $2 | awk '{print $1}'`
    echo $id
    if [ ${#id} -ne 7 ]
    then
        echo "请检查输入的name值是否正确且唯一"
    else
        /usr/bin/vagrant  $1 $id
    fi
fi


