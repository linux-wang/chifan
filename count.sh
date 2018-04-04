#!/bin/sh

dt=`date -d '+8 hours' +"%Y%m%d"`
echo $dt

curl 127.0.0.1:5000/fanfou/public_timeline/count/${dt}
