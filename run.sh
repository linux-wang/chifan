#!/bin/sh

nu=`ps -ef | grep chifan.py | wc -l`

#if [ ${nu} -ne 3 ];then
#  python chifan.py
#fi

while [ ${nu} != 3 ];do
  python chifan.py
  nu=`ps -ef | grep chifan.py | wc -l`
done
