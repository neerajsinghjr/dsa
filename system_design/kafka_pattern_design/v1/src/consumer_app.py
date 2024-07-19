from confluent_kafka import (
    Consumer, KafkaError, KafkaException
)
import streamlit as st
import pandas as pd
import numpy as np
import constants as C
import traceback
from time import sleep
import sys
import json


HEADERS = ["id", "name", "email", "created_date"]

def pretty_consumer_record(records, cols=3):
    print(f"Pretty Consumer Records : {records}")
    if records:
        df = pd.DataFrame(records,
                          columns=HEADERS)
        st.table(df)
    else:
        st.toast("No Records Found !!!")


def print_consumer_info(consumer):
    """Print information about the consumer's internal state."""
    try:
        # Print subscription information
        subscription = consumer.subscription()
        print(f"Subscribed to topics: {subscription}")

        # Print assignment information
        assignment = consumer.assignment()
        print(f"Assigned partitions: {assignment}")

        # Print metadata for all topics
        metadata = consumer.list_topics(timeout=10)
        print("Topic metadata:")
        for topic, topic_metadata in metadata.topics.items():
            print(f"Topic: {topic}, Partitions: {len(topic_metadata.partitions)}")

    except KafkaException as e:
        print(f"Error accessing consumer information: {e}")


def fetch_consumer_records(kafka_topic, kafka_server):
    conf = {
        'bootstrap.servers': kafka_server,
        'group.id': kafka_topic,
        'auto.offset.reset': C.OFFSET_SMALLEST
    }

    records = []
    consumer = Consumer(conf)

    try:
        # Producer Topic Subscription;;
        consumer.subscribe([C.PRODUCER_TOPIC])

        for _ in range(C.MAX_ITERATION):
            data = consumer.poll(timeout=1.0)

            # Producer topic any be empty;;
            if data is None:
                sleep(1)
                continue

            # Catch Error when received;;
            if data.error():
                if data.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (data.topic(), data.partition(), data.offset()))
                elif data.error():
                    raise KafkaException(data.error())
            else:
                json_raw = data.value().decode('utf-8')
                json_resp = json.loads(json_raw)
                records.append(json_resp)

                # Print consumer information after processing each message
                # print_consumer_info(consumer)

        return records

    except Exception as ex:
        print("Something Went Wrong: ", ex)
        print("Error Details: ", traceback.format_exc())

    finally:
        consumer.close()

    return records


def main():
    # Streamlit interface;;
    st.title("Sync Kafka Consumer Records")
    kafka_server = st.text_input("Kafka Server", value=C.LOCALHOST)
    kafka_topic = st.text_input("Kafka Topic", value=C.PRODUCER_TOPIC)

    if st.button("Refresh"):
        records = fetch_consumer_records(kafka_topic, kafka_server)
        pretty_consumer_record(records)
        st.success("Consumer record synced successfully!")


if __name__ == "__main__":
    main()

