from kafka import KafkaConsumer
import json

from main import db

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers='192.168.1.20:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")

    for msg in consumer:
        print("Log information = {}".format(json.loads(msg.value)))

file = open("consumer.txt", "a")
file.write("Log information = {}".format(json.loads(msg.value)))

db.session.add("consumer.txt")
db.session.commit()
