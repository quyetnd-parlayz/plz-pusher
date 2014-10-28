FROM python:2:onbuild

RUN pip install crossbar[tls,msgpack,manhole,system]

CMD ['crossbar', 'start']