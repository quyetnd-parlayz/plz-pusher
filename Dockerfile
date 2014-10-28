FROM python:2-onbuild

EXPOSE 8080

WORKDIR /usr/src/app

CMD ["crossbar", "start"]