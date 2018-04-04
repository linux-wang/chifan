#!/bin/sh

dt=`date -d 'today' +"%Y%m%d"`

curl 127.0.0.1:5000/fanfou/public_timeline/count/${dt}
