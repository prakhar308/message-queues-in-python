import time
import sys
import os
import stomp
from Listeners import MessageListener ,LoadListener




class JMS_broker:
    def __init__(self):
        self.user =  "admin"
        self.password = "password"
        self.host =  "localhost"
        self.port = 61613

    def create_connection(self):
        conn = stomp.Connection(host_and_ports = [(self.host, self.port)])
        conn.connect(login=self.user,passcode=self.password)
        return conn

    def send_msg(self,conn,destination_type,destination):
        
        p=1
        while p==1:
            msg= input("Producer :-- ")
            if(msg=="Shutdown"):
                conn.disconnect()
                break
            else:
                conn.send(body=msg, destination="/"+destination_type+"/"+destination, persistent='false',id=1) # id not added to parameter
           
        

    def receive_msg(self,destination_type,destination):
        conn = stomp.Connection(host_and_ports = [(self.host, self.port)])
        conn.set_listener('', MessageListener(conn))
        conn.connect(login=self.user,passcode=self.password)
        conn.subscribe(destination="/"+destination_type+"/"+destination, id=1, ack='auto')        ##here for set ack tag in multiple ways  
        print("Waiting for messages...")
        p=1
        while p==1: 
            time.sleep(5)

    def load_send_msg(self,conn,destination_type,destination):
        print("Sending messages")
        msg="load testing"
        p=0
        while p!=10000:
                conn.send(body=msg, destination="/"+destination_type+"/"+destination, persistent='false',id=1) # id not added to parameter
                p+=1
        

    def load_receive_msg(self,destination_type,destination):
        conn = stomp.Connection(host_and_ports = [(self.host, self.port)])
        conn.set_listener('', LoadListener(conn))
        conn.connect(login=self.user,passcode=self.password)
        conn.subscribe(destination="/"+destination_type+"/"+destination, id=1, ack='auto')        ##here for set ack tag in multiple ways  
        print("Waiting for messages...")
        p=1
        while p==1: 
            time.sleep(5)
            

    
        



if __name__ == "__main__":
    i=1
    while i==1:
        print("--1) JMS queue based messaging  \n"+
        "--2) JMS topic based broadcast \n"
        "--3)JMS Topic Load testing ")
        n=int(input())
        if(n==1):
            print("Enter the queue")
            destination=input()
            jms=JMS_broker()
            conn=jms.create_connection()
            jms.send_msg(conn,"queue",destination)
        elif(n==2):
            print("Enter the Topic")
            destination=input()
            jms=JMS_broker()
            conn=jms.create_connection()
            jms.send_msg(conn,"topic",destination)
        elif(n==3):
            print("Enter the Topic")
            destination=input()
            jms=JMS_broker()
            conn=jms.create_connection()
            jms.load_send_msg(conn,"topic",destination)
        else:
            print("--Enter Correct Option")

   