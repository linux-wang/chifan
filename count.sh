#!/bin/sh

dt=`date -d 'today' +"%Y%m%d"`
echo $dt

curl 127.0.0.1:5000/fanfou/public_timeline/count/${dt}

count=`cat ${dt}_count.txt`
content=${dt}_"${count}"

curl 127.0.0.1:5000/fanfou/chifan/${content}
