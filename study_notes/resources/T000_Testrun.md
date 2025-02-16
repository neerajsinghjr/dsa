| Feature         | Sharding | Replication |
|----------------|---------|-------------|
| **Goal**       | Distribute data across multiple servers | Copy data across multiple servers |
| **Scaling**    | Horizontal scaling | Improves read performance but not write performance |
| **Storage**    | Data is divided across shards | All nodes store the same data |
| **Use Case**   | Large datasets, high write workloads | High availability, read-heavy workloads |
| **Example**    | Large e-commerce platforms like Amazon | Backup copies for failover in banking systems |