#!/bin/sh

dt=`date -d 'today' +"%Y%m%d"`

curl 127.0.0.1:5000/fanfou/public_timeline/count/${dt}

count=`cat data/${dt}_count.txt`
content=${dt}_"${count}"

echo ${content}

curl 127.0.0.1:5000/fanfou/chifan/${content}
