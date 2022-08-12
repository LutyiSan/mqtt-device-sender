FROM   python:latest

COPY    ./device-simulator /device-simulator

RUN    pip3 install -r /device-simulator/requirements.txt

CMD    python3 device-simulator/main.py