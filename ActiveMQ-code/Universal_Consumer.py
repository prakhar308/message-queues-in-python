import time
import sys
import os
import stomp
from ActiveMQ import JMS_broker


if __name__ == "__main__":
    jms=JMS_broker()
    print("Enter the desination")
    destination = input()
    print("Enter the destination type")
    destination_type = input()
    jms.receive_msg(destination_type,destination)
    
