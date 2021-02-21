def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, 1883)
    return client
    #client.subscribe(topic)
    #client.publish(topic2, "STARTING SERVER")
    #client.publish(topic2, "CONNECTED")

