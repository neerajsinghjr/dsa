````
-------------------------------------------------------------------------------------
-> Title : System Design
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 13/07/2024
-> Updated : 16/07/2024
-> Summary : Notes indices are as follows (*** pending)
-------------------------------------------------------------------------------------
-> Q012 : Zookeeper architecture 
-> Q011 : Implementation of Kafka in Python;;
-> Q010 : Usages of Zookeeper in Kafka;;
-> Q009 : Describe use case for Kafka Offset;;
-> Q008 : What are the benefit of Kafka;;
-> Q007 : What is the purpose of Kafka;;
-> Q006 : What are the stages in Kafka;;
-> Q005 : What is the architecture of Kafka;;
-> Q004 : What is Kafka;;
-> Q003 : Database Throughput and Latency Usages;; 
-> Q002 : What is Throughput and Latency;; 
-> Q001 : Scalability in system Design;; ;;
-------------------------------------------------------------------------------------
````

### SYSTEM DESIGN NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q011 : Implementation of Kafka in Python;;

Below is an example of how you can implement a Kafka producer and consumer in
Python using the confluent-kafka library. 

This example will demonstrate the concepts of topics and partitions.


#### Installation

First, you need to install the confluent-kafka library:

> pip install confluent-kafka



### Kafka Producer Example 

The producer will send messages to a Kafka topic.


```
from confluent_kafka import Producer


# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092'  # Kafka broker
}

# Create Producer instance
producer = Producer(**conf)

# Delivery report callback function
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Produce messages to the Kafka topic 'example_topic'
for i in range(10):
    message = f"Hello Kafka {i}"
    producer.produce('example_topic', 
                      key=str(i), 
                      value=message, 
                      callback=delivery_report)
    producer.poll(0)

# Wait for any outstanding messages to be delivered 
# and delivery report callbacks to be triggered

producer.flush()


```

### Kafka Consumer Example

The consumer will read messages from the Kafka topic.


```
from confluent_kafka import Consumer, KafkaError


# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'example_group',  # Consumer group
    'auto.offset.reset': 'earliest'
}

# Create Consumer instance
consumer = Consumer(**conf)

# Subscribe to the Kafka topic 'example_topic'
consumer.subscribe(['example_topic'])

# Consume messages from the topic
try:
    while True:
        msg = consumer.poll(1.0)  # Timeout of 1 second
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('End of partition reached {0}/{1}'\
                        .format(msg.topic(), msg.partition()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print(f"Received message: {msg.value().decode('utf-8')} 
            				from topic: {msg.topic()} partition: {msg.partition()}")
finally:
    consumer.close()


```

Explanation

1) Producer:

- The producer sends messages to a Kafka topic named example_topic.

- Each message is assigned a key and a value. The delivery_report callback
  function is used to confirm message delivery.

2) Consumer:

- The consumer subscribes to the same Kafka topic example_topic.

- It polls for new messages and prints them out.

3) Topics and Partitions:

- Topic: A category to which records are sent. In this example, the topic is
  example_topic.

- Partition: A topic is divided into partitions, which allows for parallel
  processing and load balancing. Each message is sent to a specific partition
  within the topic.

When a producer sends a message, it can specify a partition or rely on Kafka's
default partitioning strategy (e.g., hash of the key).

Running the Example

- Start Kafka: Ensure that Kafka is running on your local machine or remote
  server.

- Run the Producer: Execute the producer script to send messages to the Kafka
  topic.

- Run the Consumer: Execute the consumer script to read messages from the
  Kafka topic.


-------------------------------------------------------------------------------------
### Q010 : Usages of Zookeeper in Kafka;;

Zookeeper plays a critical role in Kafka's architecture, especially in
managing distributed systems. 

Here's a practical use case to illustrate how Zookeeper is used in Kafka:


#### Use Case: Distributed Data Streaming with High Availability

Scenario:

You have a real-time data streaming platform that collects and processes large
volumes of log data from multiple web servers. You want to ensure high
availability, fault tolerance, and coordination among Kafka brokers and
consumers.

Components:

- Kafka Brokers: Handle incoming data streams, distribute partitions, and
  replicate data.

- Zookeeper: Manages metadata, coordinates brokers, handles leader election,
  and tracks consumer offsets.

- Producers: Send log data to Kafka topics.

- Consumers: Process and analyze log data in real-time.

**Step-by-Step Workflow:**

1) Broker Management:

- Kafka brokers register themselves with Zookeeper when they start.

- Zookeeper stores metadata about brokers, including their addresses and the
  topics they manage.

2) Leader Election:

- For each partition, one broker is elected as the leader, and others are
  followers.

- Zookeeper handles this election process to ensure there is always a leader
  to serve read and write requests.

- If a leader broker fails, Zookeeper initiates a new election to select a new
  leader from the followers, ensuring high availability. 

3) Metadata Management:

- Zookeeper maintains information about topic configurations, such as the
  number of partitions and their replication factors.

- When a new topic is created, or an existing topic is modified, Zookeeper
  ensures all brokers are aware of the changes. 

4) Consumer Group Coordination:

- Consumers in a group register with Zookeeper to fetch partition assignments.

- Zookeeper tracks the status of each consumer, managing rebalancing when
  consumers join or leave the group.

- This ensures that each partition is consumed by only one consumer at a time
  within the same group, distributing the workload evenly. 

5) Offset Tracking (in older Kafka versions):

- Consumers commit their offsets to Zookeeper to keep track of their position
  in each partition.

- Zookeeper stores these offsets, allowing consumers to resume from their last
  committed position in case of failure or restart.

6) Failure Detection and Recovery:

- Zookeeper continuously monitors the health of Kafka brokers and consumers.

- If a broker or consumer fails, Zookeeper quickly detects it and triggers the
  necessary recovery mechanisms, such as reassigning partitions or electing a
  new leader.


#### Example Scenario:

**Broker Startup:**

- Kafka broker B1 starts and registers with Zookeeper. Zookeeper records its
  address and available topics.

**Leader Election:**

- For topic logs with partition 0, broker B1 is elected as the leader.

**Producer Sends Data:**

A producer sends log data to partition 0 of the logs topic. The data is written to broker B1.

**Broker Failure:**

- Broker B1 (leader for partition 0) fails. Zookeeper detects this failure.

- Zookeeper initiates a leader election, and broker B2 is elected as the new
  leader for partition 0.

**Consumer Group Coordination:**

- Consumers in group log-analyzers register with Zookeeper. Zookeeper assigns
  partitions to consumers.

- Consumer C1 is assigned partition 0. It fetches data from broker B2,
  processes the logs, and commits its offsets to Zookeeper.

**Consumer Failure and Rebalancing:**

- Consumer C1 fails. Zookeeper detects the failure and reassigns partition 0
  to another consumer C2 in the group, ensuring continuous processing.


#### Benefits of Using Zookeeper with Kafka:

- High Availability: Ensures continuous operation by managing leader elections
  and broker coordination.

- Fault Tolerance: Detects and recovers from broker and consumer failures
  quickly.

- Efficient Resource Management: Coordinates and balances the load among
  brokers and consumers.

- Consistency: Maintains consistent metadata across the Kafka cluster,
  ensuring all nodes have the same view of the system.


-------------------------------------------------------------------------------------
### Q009 : Describe use case for Kafka Offset;;


#### Use Case: Order Processing System

Imagine you have an e-commerce platform with a Kafka topic named orders where
each message represents a new customer order. This topic is partitioned to
handle high throughput.


#### Components:

1) Kafka Producer: Produces messages to the orders topic whenever a new order
is placed.

2) Kafka Consumers: A group of consumers that process orders, each consumer
reading from different partitions to ensure all orders are processed.


#### Step-by-Step Workflow:

1) Producing Messages:

- Each time a customer places an order, the order details are sent to the
  orders topic.

- For example, an order with ID 12345 is produced to the topic, and Kafka
  assigns it an unique offset within its partition.

2) Consuming Messages:

- A consumer group named order-processors consists of multiple consumers, each
  consuming from different partitions of the orders topic.

- Each consumer starts reading from the latest committed offset (or from the
  beginning if it’s the first time). 

3) Processing and Committing Offsets:

- A consumer reads an order message with a specific offset (e.g., offset 42 in
  partition 1). 

- The consumer processes the order (e.g., verifies payment, updates inventory,
  and sends a confirmation email).

- After successfully processing the order, the consumer commits the offset 42
  back to Kafka. 

4) Offset Management:

- Offsets are stored in a special Kafka topic called __consumer_offsets. 

- If a consumer crashes and restarts, it reads the last committed offset and
  resumes processing from there, ensuring no order is processed more than
  once.


#### Example Scenario:

1) Order Received : Order 12345 is produced to partition 1 of the orders topic
with offset 42.

2) Consumer Reads Order : Consumer A in the order-processors group reads the
message at offset 42 from partition 1.		

3) Order Processing : Consumer A processes order 12345 (e.g., checks
inventory, processes payment).

4) Committing Offset : After successfully processing, Consumer A commits
offset 42 to Kafka.

5) Consumer Failure:

- If Consumer A crashes after processing but before committing, on restart, it
  will re-read from offset 42 to ensure order 12345 is processed.

- If Consumer A crashes after committing offset 42, it will start from offset
  43 on restart, avoiding reprocessing order 12345.



-------------------------------------------------------------------------------------
### Q008 : What are the benefit of Kafka;; 

Apache Kafka offers numerous benefits, making it a popular choice for building
real-time data pipelines and streaming applications. 

Here are some key benefits:

1. High Throughput

Kafka can handle large volumes of data with low latency. It can process
millions of messages per second, making it suitable for high-throughput
applications 

2. Fault Tolerance

Kafka ensures data durability and availability through replication. Each
partition is replicated across multiple brokers, and Kafka's distributed
architecture ensures that even if some brokers fail, the data remains
available and consistent.

3. High Performance

Kafka provides high throughput and low latency for both publishing and
consuming messages. Its efficient design and support for batch processing
enable it to deliver high performance even under heavy load.

4. Real-Time Processing

Kafka supports real-time data processing through its Streams API and
integration with stream processing frameworks like Apache Flink and Apache
Spark. This enables the creation of real-time analytics and monitoring
applications.


-------------------------------------------------------------------------------------
### Q007 : What is the purpose of Kafka;;

Apache Kafka is designed to handle large-scale, real-time data feeds. It
serves several key purposes in modern data architectures:

1. High-Throughput Messaging System

Kafka is capable of handling large volumes of data with minimal latency. It
can process millions of messages per second, making it suitable for
high-throughput use cases such as activity tracking, log aggregation, and
metrics collection.

2. Real-Time Stream Processing

With Kafka Streams, developers can create complex event-driven applications
that perform real-time computations and data transformations.

3. Data Integration

Kafka acts as a central hub for data integration, enabling the flow of data
between different systems. It allows various applications and services to
produce and consume data in a decoupled manner, making it easier to integrate
disparate systems.

4. Log Aggregation

Kafka can aggregate logs from multiple services or servers, allowing
centralized log analysis and monitoring. It provides a unified platform to
collect, store, and process log data, making it easier to diagnose issues and
gain insights into system behavior.

5. Scalability and Fault Tolerance

Kafka is designed to be horizontally scalable and fault-tolerant. It can scale
out by adding more brokers to the cluster and ensures data durability through
replication, making it resilient to failures.


-------------------------------------------------------------------------------------
### Q006 : What are the stages in Kafka;;

Apache Kafka has several stages or components that play crucial roles in its
operation. 

Here we are the primary stages

Stage 1. Message Production

This is the stage where data is generated and sent to Kafka. It involves:

	- Producers: Applications or services that send data to Kafka topics.
	  Producers can choose which partition within a topic to send the message
	  to.

	- Serialization: Data is serialized before being sent to Kafka to ensure
	  it can be efficiently transmitted and stored.


Stage 2. Message Reception and Storage

Once the messages are produced, they need to be received and stored in Kafka.
This involves:

	- Brokers: Kafka servers that receive and store data. A Kafka cluster is
	  composed of multiple brokers.

	- Topics and Partitions: Data within a topic is divided into partitions. Each
	  partition is an ordered sequence of records.

	- Replication: Partitions are replicated across multiple brokers to ensure
	  fault tolerance. Each partition has one leader and multiple followers.


Stage 3. Message Consumption

This is the stage where data is read from Kafka. It involves:

	- Consumers: Applications or services that read data from Kafka topics.
	  Consumers subscribe to topics and read data from partitions.

	- Consumer Groups: Consumers can be part of a consumer group. Each partition
	  in a topic is assigned to one consumer in a group, allowing for load
	  balancing and parallel processing.


Stage 4. Coordination and Management

To manage and coordinate the Kafka cluster, several components are involved:

	- ZooKeeper: Used by Kafka for managing and coordinating brokers, handling
	  configuration, and performing leader elections for partitions.

	- Cluster Metadata: Information about the state and configuration of the
	  Kafka cluster, such as the list of brokers, topics, and partition
	  leaders.


Stage 5. Data Processing

Kafka also supports real-time stream processing:

	- Kafka Streams: A library for building applications and microservices
	  that process data in real-time. It allows for complex event processing,
	  transformation, and enrichment of data streams.

	- Kafka Connect: A framework for connecting Kafka with external systems,
	  such as databases, key-value stores, and search indexes. It simplifies
	  the integration and data movement between Kafka and other systems.


Stage 6. Logging and Monitoring

Ensuring the smooth operation of Kafka involves:

	- Monitoring: Tools and metrics to monitor the health and performance of
	  the Kafka cluster. Common tools include Prometheus, Grafana, and Kafka
	  Manager.

	- Logging: Capturing logs for debugging and auditing purposes. Kafka logs
	  include data on broker operations, producer and consumer activities,
	  and ZooKeeper interactions.


-------------------------------------------------------------------------------------
### Q005 : What is the architecture of Kafka;;

The architecture of Apache Kafka is designed to handle high throughput,
scalability, and fault tolerance for real-time data processing. 

Here is an overview of the main components and their roles in the Kafka
architecture:

#### Kafka Workflow Lifecycle

1) Message Production
	- Producers send records to a Kafka broker.
	- Each record is written to a specific topic and partition.
	- Partitions are chosen based on a key or round-robin fashion if no key is
	  provided.

2) Message Storage

	- Messages are stored in partitions within the topic.
	- Each partition is replicated across multiple brokers for fault tolerance.
	- Each partition has a leader broker and several follower brokers.

3) Message Consumption

	- Consumers read messages from topics by subscribing to them.
	- Each consumer in a consumer group reads from a unique subset of
	  partitions.
	- Offsets keep track of the last read message.

4) Fault Tolerance

	- ZooKeeper manages broker metadata, leader elections, and health checks.
	- Replication ensures that if a broker fails, another broker can take over.


#### Kafka Core Components

1. Producers

Producers are client applications that publish (write) messages to Kafka
topics. Each message is sent to a specific topic.

2. Consumers

Consumers are client applications that subscribe to (read) messages from Kafka
topics. Consumers read messages in the order they are stored in the topic's
partitions.

3. Topics

A topic is a category or feed name to which records are stored and published.
Topics are split into partitions to enable parallel processing and
scalability.

4. Partitions

Partitions are subsets of a topic. Each partition is an ordered, immutable
sequence of records that is continually appended to—a structured commit log.
Partitions enable Kafka to scale horizontally by distributing data across
multiple brokers.

5. Brokers

Brokers are Kafka servers that store data and serve client requests. A Kafka
cluster is composed of multiple brokers to ensure scalability and fault
tolerance.

6. Clusters

A Kafka cluster consists of multiple brokers. Clusters are managed by
ZooKeeper, which coordinates brokers and handles leader election for
partitions.

7. ZooKeeper

ZooKeeper is used by Kafka to manage distributed configurations and
synchronization. It helps with broker leader election and metadata storage.

8. Replication

To ensure reliability and fault tolerance, Kafka replicates partitions across
multiple brokers. Each partition has one leader and multiple followers. The
leader handles all read and write requests, while followers replicate the
data.

9. Kafka Connect

Kafka Connect is a framework to import and export data from/to other systems.
Connectors are used to move large collections of data in and out of Kafka.

10. Kafka Streams

Kafka Streams is a library for building streaming applications that process
data in real-time. It uses Kafka as the underlying data source and sink.


-------------------------------------------------------------------------------------
### Q003 : What is Kafka;;

- Apache Kafka is an open-source stream-processing software platform developed
  by LinkedIn and donated to the Apache Software Foundation, written in Scala
  and Java. 

- Kafka is designed to handle real-time data feeds, providing a
  high-throughput, low-latency platform for handling real-time data and
  integrating large amounts of data from many sources.


#### Real Life Use Cases:

1) Real-Time Analytics: Processing data streams in real-time for analytics and
monitoring.

2) Data Integration: Integrating data from multiple sources and storing it in
different target systems.

3) Event Sourcing: Recording state changes as a sequence of events.

4) Log Aggregation: Collecting and aggregating log data from different systems
in a centralized manner.


-------------------------------------------------------------------------------------
### Q002 : What is Throughput and Latency;;

Reference: https://aws.amazon.com/compare/the-difference-between-throughput-and-latency/



-------------------------------------------------------------------------------------
### Q001 : Scalability in system Design;;

Reference: https://newsletter.ashishps.com/p/scalability




-------------------------------------------------------------------------------------