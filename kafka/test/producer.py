import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    security_protocol="SASL_PLAINTEXT",  
    sasl_mechanism="PLAIN",
    sasl_plain_username="admin",
    sasl_plain_password="admin-secret",
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

topic_name = 'sample_topic'
message = {
    "event": "Hi there",
}
try:
    future = producer.send(topic_name, value=message)
    record_metadata = future.get(timeout=10)
    print(f"Topic: {record_metadata.topic}")
    print(f"Partition: {record_metadata.partition}")
    print(f"Offset: {record_metadata.offset}")
except KafkaError as e:
    print(f"Error sending message: {e}")
finally:
    producer.close()
    print("Producer closed.")
