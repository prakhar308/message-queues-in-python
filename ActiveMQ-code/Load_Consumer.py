import time
import sys
import os
import stomp

from ActiveMQ import JMS_broker


if __name__ == "__main__":
    jms=JMS_broker()
    print("Enter the Topic")
    destination = input()
    jms.load_receive_msg("topic",destination)
   
