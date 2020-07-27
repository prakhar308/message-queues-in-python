from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers = 'localhost:9092')

while True:
    print("\n\nType \"quit\" to exit")
    print("Enter message to be sent:")
    msg = input()
    if msg == "quit":
        print("Exiting")
        break
    producer.send('Hello-everyone', msg.encode('utf-8'))
    print("Sending msg \"{}\"".format(msg))

    metric = producer.metrics(raw=False)
    print(metric)
    print('\nThe Producer metrics : ')
    print('Request size max : ')
    print(metric['producer-metrics']['request-size-max'])
    print('\nKafka-metrics-count : ')
    print(metric['kafka-metrics-count'])

    print(metric.keys())

print("Message sent!")
