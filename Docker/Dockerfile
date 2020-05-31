#pip freeze > requirements.txt
#docker build -t dev_ubuntu . 
#docker run -it dev_ubuntu bin/bash
FROM ubuntu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-venv -y
RUN apt-get install git -y
RUN apt-get install vim -y
RUN git config --global user.email "kingwan111@gmail.com"
RUN git config --global user.name "wani111"
RUN git clone https://github.com/wani111/stock1.git /home/app
WORKDIR /home/app/stock1
RUN git pull
WORKDIR /home/app
RUN python3 -m venv venv
RUN . ./venv/bin/activate && pip install wheel && pip install -r requirements.txt


