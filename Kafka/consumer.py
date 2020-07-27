from kafka import KafkaConsumer


consumer = KafkaConsumer('Hello-everyone')

for message in consumer:
    msg = str(message.value.decode())
    print("Writing message %s " % msg)

    metric = consumer.metrics(raw=False)
    print(metric)
    print('\n\nThe Consumer Fetch Manager metrics : ')
    print('Fetch latency max : ')
    print(metric['consumer-fetch-manager-metrics']['fetch-latency-max'])
    print('Bytes-consumed-rate : ')
    print(metric['consumer-fetch-manager-metrics']['bytes-consumed-rate'])
    print('Fetch-size-max: ')
    print(metric['consumer-fetch-manager-metrics']['fetch-size-max'])
    print('\nKafka-metrics-count : ')
    print(metric['kafka-metrics-count'])
    print('\nThe Consumer metrics : ')
    print('Consumer-metric Request-size-max: ')
    print(metric['consumer-metrics']['request-size-max'])

    print(metric.keys())
