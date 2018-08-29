FROM dockerhub.datagrand.com/global/centos:7.2.1511

#作者标签，有问题就找他
LABEL maintainer "v_v"

#环境变量硬编码及时区
ENV ENVIRONMENT production
RUN cd / && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#yum 基础工具，记住clean
RUN yum clean all \
    && yum makecache \
    && yum install -y wget gcc gcc-c++ python-devel mysql-devel bzip2 make \
    && yum clean all

#pip 基础工具及版本
RUN yum install -y epel-release \
    && yum install -y python-pip \
    && yum clean all \
    && pip install --upgrade pip -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com \
    && pip install setuptools==33.1.1 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com     

#守护进程，可配置多进程，推荐但不必须，各位大佬自己定
#RUN yum install -y python-setuptools \
#    && pip install supervisor -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com \
#    && mkdir -m 755 -p /etc/supervisor/conf.d 
#    COPY supervisor.conf /etc/supervisor/supervisord.conf

#镜像启动命令 
#CMD ["supervisord","-c","/etc/supervisor/supervisord.conf"]

RUN mkdir -p /home/chifan
COPY . /home/chifan

#pip 依赖
RUN pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r /home/chifan/requirements.txt

WORKDIR /home/chifan/src

EXPOSE 22
EXPOSE 5000

CMD ["python","chifan.py"]
