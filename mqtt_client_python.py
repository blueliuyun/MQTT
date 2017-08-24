# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:26:41 2017

@author: Tian
"""
import paho.mqtt.client as mqtt

#
def on_connect(client, obj, flags, rc):
    print("connected with rc: "+str(rc))
    #client.subscribe("test/topic")

def on_message(client, obj, msg):
    print("on_message")
    print(msg.topic + " received message: " +str(msg.payload))
    
def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("subscribed: " + str(mid))


def on_log(client, obj, level, string):
    print(string)

#
client = mqtt.Client(client_id="ye")
client.on_connect = on_connect
client.on_message = on_message
#client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.connect("127.0.0.1", 1883, 60)
#client.connect("m2m.eclipse.org", 1883, 60)
subResult = client.subscribe("test/topic", 0)
subResult = client.publish("test/topic", "1205")

client.loop_forever()


#client.loop_forever(timeout=1)
