FROM   python:latest

COPY    ./simulator /simulator

RUN    pip3 install -r /simulator/requirements.txt

CMD    python3 /main.py