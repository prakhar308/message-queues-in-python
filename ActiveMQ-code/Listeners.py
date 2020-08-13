import time
import sys
import os
import stomp
class MessageListener(object):						#Listener has function defined which are provoked when certain task is done
  
	def __init__(self, conn):
		self.conn = conn
		self.count = 0
		self.start = time.time()
	def on_error(self, headers, message):
		print('received an error %s' % message)
	def on_message(self, headers, message):
                self.start = time.time()
                self.count += 1
                print("Received  :--"+message)
                if message == "SHUTDOWN":
                        diff = time.time() - self.start
                        print("Received %s in %f seconds" % (self.count, diff))
                        self.conn.disconnect()
                        sys.exit(0)
                else:
                        if self.count%1000 == 0:
                                print("Received %s messages." % self.count)
class LoadListener(object):						#Listener has function defined which are provoked when certain task is done
    def __init__(self, conn):
        self.conn = conn
        self.count = 0
        self.start = time.time()
        self.flag = 0
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        if(self.flag==0):
            self.flag=1
            self.start=time.time()
        self.count += 1
        diff = time.time() - self.start
        if self.count==10000:
                print("Received %s in %f seconds" % (self.count, diff))
                rate=1000/diff
                print(str(rate)+"per sec")
                self.conn.disconnect()
                sys.exit(0)
        