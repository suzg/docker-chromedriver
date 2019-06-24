FROM ubuntu:18.04
MAINTAINER suzg

ADD sources.list /etc/apt/

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
	LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y \
		wget unzip python3 python3-dev python3-pip \
        fonts-wqy-zenhei && \
	wget --progress=bar:force:noscroll https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /chrome.deb && \
	apt-get install -y /chrome.deb && \
	rm -rf /var/lib/apt/lists/* && \
	rm /chrome.deb

ADD pip.conf /root/.pip/
RUN pip3 install -U pip

ADD requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

RUN wget --progress=bar:force:noscroll https://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_linux64.zip -O /chromedriver.zip && \
    cd /usr/local/bin && unzip /chromedriver.zip && \
    rm /chromedriver.zip

ENV PYTHONIOENCODING=utf-8
