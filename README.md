plz-pusher
==========

Simple HTTP to Websocket Pusher

##Quickstart

```shell
pip install -r requirements.txt
crossbar start
#test pusher
curl -H "Content-Type: application/json" -d '{"topic": "com.myapp.topic1", "args": ["Hello, world"]}' http://127.0.0.1:8080/push
```
