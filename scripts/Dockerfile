FROM jjanzic/docker-python3-opencv 

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]