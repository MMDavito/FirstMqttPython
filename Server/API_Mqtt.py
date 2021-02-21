#!/usr/bin/python3
from flask import Flask, request,jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

topic = 'foo'
topic2 = 'bar'
port = 5000

def on_connect(client, userdata, flags,rc):
    print("Flaggor: ",flags)
    print("Connecting paho")
    client.subscribe(topic)
    client.publish(topic2, "STARTING SERVER")
    client.publish(topic2, "CONNECTED")
    print("Connecting paho port: ",client._port)
    print("Broker is: ",client._host)


def on_message(client, userdata, msg):
    client.publish(topic2, "MESSAGE")

def msgToMq(client, msg):
    client.publish(topic, msg,retain=True)


@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)

@app.route("/msg",methods=['POST'])
def msg_publish():
    content = request.json
    print("Content: ",content)
    print("JSON:",content["msg"])
    msgToMq(client,content["msg"])
    return "OK"

if __name__ == '__main__':
    client = mqtt.Client()
    #client.username_pw_set(username, password)
    client.retain=True
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('localhost')
    client.loop_start()

    app.run(host='0.0.0.0', port=port)