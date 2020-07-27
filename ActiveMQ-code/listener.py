import time
import sys
import os
import stomp

user =  "admin"
password = "password"
host =  "localhost"
port = 61613
destination =  ["/topic/quility"] ##["/queue/profile]----->Here u can shift from topic to queue
destination = destination[0]

class MyListener(object):						#Listener has function defined which are provoked when certain task is done
  
	def __init__(self, conn):
		self.conn = conn
		self.count = 0
		self.start = time.time()
	def on_error(self, headers, message):
		print('received an error %s' % message)
	def on_message(self, headers, message):
		if message == "SHUTDOWN":
			diff = time.time() - self.start
			print("Received %s in %f seconds" % (self.count, diff))
			
			conn.disconnect()
			sys.exit(0)
		else:
			if self.count==0:
				self.start = time.time()
				self.count += 1
			if self.count % 1000 == 0:
				print("Received %s messages." % self.count)
		if message =="ask":
				print("sending ACK")
				self.conn.ack(id=headers.get("message-id"),subscription=headers.get("subscription"))    #sending acknowledge 
			

conn = stomp.Connection(host_and_ports = [(host, port)])
print(conn)
conn.set_listener('', MyListener(conn))
conn.connect(login=user,passcode=password)
conn.subscribe(destination=destination, id=1, ack='auto')        ##here for set ack tag in multiple ways  
print("Waiting for messages...")
while 1: 
  time.sleep(10) 