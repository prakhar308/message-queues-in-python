# message-queues-in-python

Table of Contents
-----------------

- [What are Message Queues](#What-are-Message-Queues)
- Different Message Queues:
    + [RabbitMQ](#RabbitMQ)
    + [Kafka](#Kafka)
    + [ActiveMQ](#ActiveMQ)


What are Message Queues
--------

Message queuing allows applications to communicate by sending messages to each other.The message queue provides temporary message storage when the destination program is busy or not connected.

![Message Queue Architecture](Images/message-queue-architecture.jpg)

The basic architecture of a message queue is simple; there are **client** applications called **producers** that create messages and deliver them to the message **queue**. Another application, called a **consumer**, connects to the queue and gets the messages to be processed. Messages placed onto the queue are stored until the consumer retrieves them.

A message queue provides an **asynchronous communications protocol**, which is a system that puts a message onto a message queue and does not require an immediate response to continuing processing. **Email** is probably the best example of asynchronous communication. When an email is sent, the sender continues to process other things without needing an immediate response from the receiver. This way of handling messages **decouples** the producer from the consumer so that they do not need to interact with the message queue at the same time.


[RabbitMQ](https://www.rabbitmq.com/)
--------

RabbitMQ is a message broker: it accepts and forwards messages.

RabbitMQ, and messaging in general, uses some jargon.

- **Producing** means nothing more than sending. A program that sends messages is a **producer** 
- A **queue** is the name for a post box which lives inside RabbitMQ. Although messages flow through RabbitMQ and your applications, they can only be stored inside a queue. A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer.
- **Consuming** has a similar meaning to receiving. A **consumer** is a program that mostly waits to receive messages

#### Quick start (using the Pika Python client):

[Install RabbitMQ](https://www.rabbitmq.com/download.html)

Install Pika - RabbitMQ Python Client:
```bash
python -m pip install pika --upgrade
```

#### Code

A producer (sender) that sends a single message, and a consumer (receiver) that receives messages and prints them out. It's a "Hello World" of messaging.

You can find the code [here](RabbitMQ-Code)

[Tutorial: "Hello World!"](https://www.rabbitmq.com/tutorial-one-python.html):
    
```bash
python send.py
python receive.py
```

#### RabbitMQ Features:

- **Round-robin dispatching**: [Tutorial](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
    + By default, RabbitMQ will send each message to the next consumer, in sequence. On average every consumer will get the same number of messages. This way of distributing messages is called round-robin. 
    + This helps is easily parallelise work. If we are building up a backlog of work, we can just add more consumers and that way, scale easily.

- **Message acknowledgement**: [Tutorial](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
    + An **ack(nowledgement)** is sent back by the consumer to tell RabbitMQ that a particular message had been received, processed and that RabbitMQ is free to delete it.
    + If a consumer dies without sending an ack, RabbitMQ will re-queue it. If there are other consumers online at the same time, it will then quickly redeliver it to another consumer. 

- **Message Durability**: [Tutorial](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
    + we can mark both the queue and messages as durable.

- **Fair dispatch**: [Tutorial](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
    + In a situation with two workers, when all odd messages are heavy and even messages are light, one worker will be constantly busy and the other one will do hardly any work. 
    + In order to defeat RabbitMQ allows us to use the `Channel#basic_qos` channel method with the `prefetch_count=1` setting. This uses the `basic.qos` protocol method to tell RabbitMQ not to give more than one message to a worker at a time

- **Exchanges**:
    + The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue.
    + Instead, the producer can only send messages to an exchange.
    + An exchange receives messages from producers and the other side it pushes the to the queue.
    
    ![Exchange](Images/exchanges.png)
    + Here X is an exchange
    + It allows us to send message to multiple consumers
    
    + Types:
        * fanout - it broadcast all the messages it receives to all the queues [Tutorial](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)
        * direct - send message to a particular queue [Tutorial](https://www.rabbitmq.com/tutorials/tutorial-four-python.html)
        * topic - send message to all the queues which matches the topic [Tutorial](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)

### Monitoring

- Run [rabbitmq-monitoring.py](RabbitMQ-Code/rabbitmq-monitoring.py)
```bash
python rabbitmq-monitoring.py
```
- The default username/password is guest/guest
- Monitoring is performed by accessing RabbitMQ's HTTP API
- Output Example:

![RabbitMQ-monitoring](Images/rabbitmq-monitoring.png)

- It displays:
    + Overview: queue name and state(idle/running)
    + No.of messages : ready, unacknowledged and total
    + Rate: incoming/publish
- Every 5 seconds the monitoring output is updated