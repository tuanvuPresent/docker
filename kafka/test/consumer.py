from kafka import KafkaConsumer

# Kafka Consumer setup with SASL authentication
consumer = KafkaConsumer(
    'sample_topic',                   
    bootstrap_servers=['localhost:9092'],
    security_protocol="SASL_PLAINTEXT",  
    sasl_mechanism="PLAIN",               
    sasl_plain_username="admin", 
    sasl_plain_password="admin-secret",
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sample_group'
)

try:
    for message in consumer:
        print(f"message: {message}")
except KeyboardInterrupt:
    print("Consumer interrupted.")
finally:
    consumer.close()
    print("Consumer closed.")
