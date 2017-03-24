# Set the base image to Ubuntu
FROM continuumio/miniconda3

RUN conda install -q -y pandas requests

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@gmail.com"

ADD ./config /pyrest/config
ADD ./pyserver /pyrest/pyserver
ADD ./start.py /pyrest/start.py

WORKDIR pyrest

EXPOSE 8000

# install Python environment
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt && rm requirements.txt

CMD python /pyrest/start.py
