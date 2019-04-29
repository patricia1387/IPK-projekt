#!/bin/env python3

import sys
import socket
import json
from socket import *

if len(sys.argv) != 3:
        sys.stderr.write("Wrong number of arguments\n")
        sys.exit()

CITY = sys.argv[2]
API_KEY = sys.argv[1]
HOST = "api.openweathermap.org" 

message = 'GET /data/2.5/weather?q='+CITY+'&APPID='+API_KEY+'&units=metric HTTP/1.1\r\nHost:'+HOST+'\r\n\r\n'
message = str.encode(message)



HOST = "api.openweathermap.org" 
PORT = 80 
mySocket = socket(AF_INET, SOCK_STREAM)
mySocket.connect((HOST,PORT))
mySocket.sendall(message)
data = mySocket.recv(1024).decode()
data.json.loads(data[data.find("\r\n\r\n")+4:])


try:
	description = data['weather'][0]['description']
	temp = data['main']['temp']
	pressure = data['main']['pressure']
	humidity = data['main']['humidity']
	wind_speed = data['wind']['speed']*3.6
	wind_deg = data['wind']['deg']

	print(CITY)
	print('{}'.format(description))
	print('Teplota : {} stupnov Celzia'.format(temp))
	print('Tlak : {} hPa'.format(pressure))
	print('Vlhkost : {} %'.format(humidity))
	print('Rychlost vetra : {} km/h'.format(wind_speed))
	print('Smer vetra : {} '.format(wind_deg))
except:
	print("Mesto sa nenašlo: " + CITY)

