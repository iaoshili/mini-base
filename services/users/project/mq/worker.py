from kafka import KafkaConsumer

consumer = KafkaConsumer('sample', bootstrap_servers='kafka:9093')
for msg in consumer:
    print(msg)
