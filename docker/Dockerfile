FROM ubuntu:18.04
MAINTAINER suzg

ADD sources.list /etc/apt/

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
	LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y \
		curl wget unzip python3 python3-dev python3-pip \
        fonts-wqy-zenhei build-essential imagemagick && \
	wget --progress=bar:force:noscroll https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /chrome.deb && \
	apt-get install -y /chrome.deb && \
	rm -rf /var/lib/apt/lists/* && \
	rm /chrome.deb

ADD pip.conf /root/.pip/
RUN pip3 install -U pip

ADD requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

RUN CHROME_VER=`apt list 2>/dev/null | grep google-chrome-stable | awk '{print $2}' | awk -F. '{printf "%s.%s.%s",$1,$2,$3}'` && \
    VER_URL=https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VER && \
    DRIVER_VER=`curl $VER_URL` && \
    wget --progress=bar:force:noscroll https://chromedriver.storage.googleapis.com/$DRIVER_VER/chromedriver_linux64.zip -O /chromedriver.zip && \
    cd /usr/local/bin && unzip /chromedriver.zip && \
    chmod 755 /usr/local/bin/chromedriver && \
    rm /chromedriver.zip

ENV PYTHONIOENCODING=utf-8

ADD TerminalImageViewer /TerminalImageViewer
RUN cd /TerminalImageViewer/src/main/cpp && make && make install && cd / && rm -rf /TerminalImageViewer
ENV TERM=xterm-256color

