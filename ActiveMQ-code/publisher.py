import sys
import os
import stomp
import time

user = "admin"
password = "password"
host ="localhost"
port = 61613
destination =  ["/topic/ishan"]
destination = destination[0]

messages = 10000
data = "Data From Stomp"

conn = stomp.Connection(host_and_ports = [(host, port)])
conn.connect(login=user,passcode=password)
for i in range(0, messages):
  conn.send(body=data, destination="/topic/ishan", persistent='false',id=i)
while i!=10: 
  time.sleep(3)
  conn.send(body="ask", destination=destination, persistent='false',ack='client')
  i=10
conn.send(body="SHUTDOWN", destination=destination, persistent='false')

conn.disconnect()