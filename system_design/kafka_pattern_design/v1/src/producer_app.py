from confluent_kafka import Producer
import streamlit as st
import constants as C
import socket
import json


# ProducerApp:
# It will accept multiple json files and send the json
# file content to kafka broker;;


def json_data_generator(uploaded_files):
    for uploaded_file in uploaded_files:
        json_data = json.load(uploaded_file)
        if isinstance(json_data, list):
            for record in json_data:
                yield record
        else:
            yield json_data


def kafka_logger(err, msg):
    """Called once for each message produced to indicate delivery result.
       Triggered by poll() or flush()."""
    if err is not None:
        st.error(f'Message delivery failed: {err}')
    else:
        st.info(f'Message delivered to {msg.topic()} [{msg.partition()}]')


def kafka_producer_generator(json_data_generator, kafka_topic, kafka_server):
    # Set up Kafka producer
    conf = {
        'bootstrap.servers': kafka_server,
        'client.id': socket.gethostname() # beyond-infinity in our example;;
    }
    producer = Producer(**conf)

    for record in json_data_generator:
        producer.produce(kafka_topic,
                         key=str(record.get('id', '')),
                         value=json.dumps(record),
                         callback=kafka_logger)
        # Wait up to 1 second for events. Callbacks will be invoked
        # during this method call if the message is acknowledged.
        producer.poll(0)

    producer.flush()


def main():
    # Streamlit interface;;
    st.title("JSON File Uploader")
    uploaded_files = st.file_uploader("Choose JSON files", type="json",
                                      accept_multiple_files=True)

    kafka_server = st.text_input("Kafka Server", value=C.LOCALHOST)
    kafka_topic = st.text_input("Kafka Topic", value=C.PRODUCER_TOPIC)

    if uploaded_files and st.button("Send to Kafka"):
        json_generator = json_data_generator(uploaded_files)
        kafka_producer_generator(json_generator, kafka_topic, kafka_server)
        st.success("JSON data sent to Kafka successfully!")


if __name__ == "__main__":
    main()

