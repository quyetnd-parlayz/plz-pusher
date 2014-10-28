import crossbarconnect


if __name__ == '__main__':
    ## Create a new Crossbar.io push client (once), providing key/secret
    ##
    client = crossbarconnect.Client("http://127.0.0.1:8080/push")

    ## Publish an event with (positional) payload and get publication ID
    ## Since we provided key/secret before, the request will be signed.
    ##
    event_id = client.publish("com.myapp.topic1", "Hello, world!", 23, 456, 7889)

    print("event published with ID {0}".format(event_id))
