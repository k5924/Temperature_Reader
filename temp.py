from gpiozero import CPUTemperature
import sched, time
import paho.mqtt.client as mqtt
import os

client = mqtt.Client()

username = 'paks'
password = 'paks'
broker_ip = '127.0.0.1'
broker_port = 1883
topic = 'temperature'

s = sched.scheduler(time.time, time.sleep)

def getTemp(sc):
	client.username_pw_set(username, password)
	client.connect(broker_ip, broker_port, 10)

	cpu = CPUTemperature()
	client.publish(topic, float(cpu.temperature))
	
	s.enter(10, 1, getTemp, (sc,))

s.enter(10, 1, getTemp, (s,))
s.run()
