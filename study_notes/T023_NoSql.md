````
------------------------------------------------------------------------------------
-  Title : NoSql Notes
-  Author : @neeraj-singh-jr
-  Status : Ongoing...
-  Created : 10/02/2025
-  Updated : 15/02/2025
-  Summary : Notes indices are as follows (**** pending)
------------------------------------------------------------------------------------
-> Q007 : Syntex for writing MongoDB Query;;
-> Q006 : MongoDB Queries Using Python;;
-> Q005 : MongoDB Query Fundamentals;;
-> Q004 : What is Sharding in DBMS;;
-> Q003 : MongoDB System Design Considerations;;
-> Q002 : MongoDB Core Architecture;;
-> Q001 : Introduction to NoSql;;
------------------------------------------------------------------------------------
````

### NOSQL NOTES : BEGINNING

------------------------------------------------------------------------------------
### Q007 : Syntex for writing MongoDB Query;;

#### **Basic MongoDB Query Syntax**

In MongoDB, queries are written using **JSON-like documents**. Below are the
fundamental query syntaxes:

---

#### **1. Find Documents (`SELECT` equivalent)**

```js
db.collection.find({ field: value })
```

- **Example:** Find users with age **25**.

```js
db.users.find({ age: 25 })
```

- **Find all documents (like `SELECT *`)**:

```js
db.users.find({})
```

- **Find with multiple conditions (`AND`)**:

```js
db.users.find({ age: 25, city: "Delhi" })
```

---

#### **2. Insert Document (`INSERT` equivalent)**

```js
db.collection.insertOne({ key1: value1, key2: value2 })
db.collection.insertMany([{ key1: value1 }, { key1: value2 }])
```

🔹 **Example: Insert a single user**:

```js
db.users.insertOne({ name: "John", age: 30, city: "New York" })
```

🔹 **Insert multiple users**:

```js
db.users.insertMany([
    { name: "Alice", age: 28 },
    { name: "Bob", age: 35 }
])
```

---

#### **3. Update Document (`UPDATE` equivalent)**

```js
db.collection.updateOne({ filter }, { $set: { field: new_value } })
db.collection.updateMany({ filter }, { $set: { field: new_value } })
```

🔹 **Example: Update Alice's age to 29**:

```js
db.users.updateOne({ name: "Alice" }, { $set: { age: 29 } })
```

🔹 **Update multiple documents**:

```js
db.users.updateMany({ age: { $lt: 30 } }, { $set: { status: "young" } })
```

---

#### **4. Delete Document (`DELETE` equivalent)**

```js
db.collection.deleteOne({ filter })
db.collection.deleteMany({ filter })
```

🔹 **Delete a specific user**:

```js
db.users.deleteOne({ name: "Bob" })
```

🔹 **Delete all users above age 40**:

```js
db.users.deleteMany({ age: { $gt: 40 } })
```

---

#### **5. Sorting & Limiting Results**

```js
db.collection.find().sort({ field: 1 })   // Ascending (1) or Descending (-1)
db.collection.find().limit(number)
```

🔹 **Sort users by age (ascending)**:

```js
db.users.find().sort({ age: 1 })
```

🔹 **Limit results to top 5 users**:

```js
db.users.find().limit(5)
```

---

#### **Bonus: Aggregation (Advanced Queries)**

```js
db.collection.aggregate([
    { $match: { field: value } },
    { $group: { _id: "$field", total: { $sum: "$another_field" } } }
])
```

🔹 **Example: Count users per city**:

```js
db.users.aggregate([
    { $group: { _id: "$city", total: { $sum: 1 } } }
])
```

---

#### **✅ Summary**

| SQL Equivalent                                      | MongoDB Query                                                  |
| --------------------------------------------------- | -------------------------------------------------------------- |
| `SELECT * FROM users`                               | `db.users.find({})`                                            |
| `SELECT * FROM users WHERE age=25`                  | `db.users.find({ age: 25 })`                                   |
| `INSERT INTO users (name, age) VALUES ('John', 30)` | `db.users.insertOne({ name: "John", age: 30 })`                |
| `UPDATE users SET age=29 WHERE name='Alice'`        | `db.users.updateOne({ name: "Alice" }, { $set: { age: 29 } })` |
| `DELETE FROM users WHERE name='Bob'`                | `db.users.deleteOne({ name: "Bob" })`                          |


------------------------------------------------------------------------------------
#### Q006 : MongoDB Queries Using Python;;

This section revolves how to **use Python to interact with MongoDB** using
the **pymongo** library.

We will cover:

- Connecting Python to MongoDB
- Performing CRUD operations
- Using advanced queries
- Working with indexes
- Handling aggregation

---

#### **1. Installing & Setting Up PyMongo**

First, install the **pymongo** library:

```bash
pip install pymongo
```

Now, import the library and establish a connection:

```python
from pymongo import MongoClient

# Connect to MongoDB (Default port: 27017)
client = MongoClient("mongodb://localhost:27017/")

# Create or select a database
db = client["my_database"]

# Create or select a collection (similar to a table in SQL)
collection = db["users"]

print("MongoDB Connected!")
```

---

#### **2. Insert Operations (CREATE - DML)**

We can insert single or multiple documents into a MongoDB collection.

#### **Insert One Document**

```python
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}
collection.insert_one(user)
print("Inserted One Document")
```

#### **Insert Multiple Documents**

```python
users = [
    {"name": "Bob", "age": 30, "email": "bob@example.com"},
    {"name": "Charlie", "age": 28, "email": "charlie@example.com"}
]
collection.insert_many(users)
print("Inserted Multiple Documents")
```

---

#### **3. Read Operations (READ - DML)**

MongoDB uses `.find()` and `.find_one()` to retrieve data.

#### **Fetch All Documents**

```python
for user in collection.find():
    print(user)
```

#### **Fetch One Document**

```python
user = collection.find_one({"name": "Alice"})
print(user)
```

#### **Query with Conditions**

```python
# Users older than 25
for user in collection.find({"age": {"$gt": 25}}):
    print(user)
```

#### **Query with AND / OR Conditions**

```python
# AND condition: Users named "Alice" AND age > 20
for user in collection.find({"name": "Alice", "age": {"$gt": 20}}):
    print(user)

# OR condition: Users named "Bob" OR "Charlie"
for user in collection.find({"$or": [{"name": "Bob"}, {"name": "Charlie"}]}):
    print(user)
```

---

### **4. Update Operations (UPDATE - DML)**

MongoDB allows **updating single or multiple documents** using `update_one()`
and `update_many()`.

#### ** Update One Document**

```python
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
print("Updated Alice's Age")
```

#### **Update Multiple Documents**

```python
collection.update_many({}, {"$inc": {"age": 1}})  # Increase age by 1 for all users
print("Updated Age for All Users")
```

---

#### **5. Delete Operations (DELETE - DML)**

We can delete single or multiple documents.

#### **Delete One Document**

```python
collection.delete_one({"name": "Alice"})
print("Deleted Alice")
```

#### **Delete Multiple Documents**

```python
collection.delete_many({"age": {"$gt": 30}})
print("Deleted Users Older Than 30")
```

---

#### **6. Advanced Queries & Indexing**

#### **Sorting Results**

```python
for user in collection.find().sort("age", -1):  # Sort by age (Descending)
    print(user)
```

#### **Limiting Results**

```python
for user in collection.find().limit(5):  # Limit to 5 results
    print(user)
```

#### **Creating Indexes for Performance**

```python
collection.create_index("email", unique=True)
print("Created Index on Email")
```

---

#### **7. Aggregation (Advanced Queries)**

Aggregation allows **grouping and processing** data like SQL `GROUP BY`.

#### **Grouping Users by Age**

```python
pipeline = [
    {"$group": {"_id": "$age", "count": {"$sum": 1}}}
]
for group in collection.aggregate(pipeline):
    print(group)
```

#### **Using `$match` and `$project` in Aggregation**

```python
pipeline = [
    {"$match": {"age": {"$gt": 25}}},  # Filter: Age > 25
    {"$project": {"_id": 0, "name": 1, "age": 1}}  # Show only name & age
]
for user in collection.aggregate(pipeline):
    print(user)
```

---

#### **8 Handling Transactions (Atomic Operations)**

MongoDB supports transactions for **multi-document operations**.

```python
with client.start_session() as session:
    with session.start_transaction():
        collection.insert_one({"name": "Eve", "age": 24}, session=session)
        collection.update_one({"name": "Bob"}, {"$set": {"age": 32}}, session=session)
    print("Transaction Completed")
```

------------------------------------------------------------------------------------
### Q005 : MongoDB Query Fundamentals;;

#### **Introduction to MongoDB Compass**

MongoDB Compass is a **graphical user interface (GUI) tool** that allows you
to **interact with MongoDB without using the command line**.

#### **How to Install MongoDB Compass**

1. Download MongoDB Compass from [MongoDB Official Website]
   (https://www.mongodb.com/try/download/compass)
2. Install and open it.
3. Connect to your MongoDB instance by entering the **MongoDB connection
   string** (e.g., `mongodb://localhost:27017`).

---

#### **2. DDL (Data Definition Language) - Creating & Managing Database

#### **1. Creating a New Database**

- **Syntax in Compass (GUI):**

  - Click on **"Create Database"** in MongoDB Compass.
  - Enter **Database Name** and **Collection Name** (like a table in SQL).
  
- **Syntax in MongoDB Shell:**

    ```js
    // Switch to database (creates it if it doesn’t exist)
    use my_database;  
    ```

---

#### **2. Creating a Collection (Equivalent to Tables in SQL)**

- **Compass:** Click on **"Create Collection"**, enter the **name** and
  click **Create**.

- **MongoDB Shell:**

    ```js
    db.createCollection("users");
    ```
  
- **To list all collections:**

    ```js
    show collections;
    ```

---

#### **3. Dropping a Database**

- **Compass:** Click on the **database name**, then **"Drop Database"**.

- **MongoDB Shell:**
    ```js
    use my_database;
    db.dropDatabase();
    ```

---

#### **4. Dropping a Collection**

- **Compass:** Click on the **collection name**, then **"Drop Collection"**.

- **MongoDB Shell:**
  ```js
  db.users.drop();
  ```

---

#### **3. DML (Data Manipulation Language) - CRUD Operations**

Now, let's see how to **insert, update, delete, and query data**.

---

#### **1. Inserting Data (INSERT)**

#### **📌 Insert One Document**

- **Compass:** Open the collection → Click on **"Insert Document"** → Add a
  JSON document.
- **MongoDB Shell:**
  ```js
  db.users.insertOne({
      name: "Alice",
      age: 25,
      email: "alice@example.com"
  });
  ```

#### **Insert Multiple Documents**

- **MongoDB Shell:**
  ```js
    db.users.insertMany([
        { name: "Bob", age: 30, email: "bob@example.com" },
        { name: "Charlie", age: 28, email: "charlie@example.com" }
    ]);
  ```

---

#### **2. Querying Data (SELECT)**

#### **Fetch All Documents**

- **Compass:** Click **"Find"** to retrieve all documents.
- **MongoDB Shell:**
  ```js
  db.users.find();
  ```

#### **Find a Specific Document**

- **MongoDB Shell:**
  ```js
  db.users.findOne({ name: "Alice" });
  ```

#### **Query with Conditions**

- **Find users older than 25:**

  ```js
  db.users.find({ age: { $gt: 25 } });
  ```
- **Find users named Bob or Charlie:**

  ```js
  db.users.find({ name: { $in: ["Bob", "Charlie"] } });
  ```
- **Find users with age between 20 and 30:**

  ```js
  db.users.find({ age: { $gte: 20, $lte: 30 } });
  ```

---

### **3. Updating Data (UPDATE)**

#### **Update One Document**

- **Change Alice’s age to 26:**
  ```js
  db.users.updateOne({ name: "Alice" }, { $set: { age: 26 } });
  ```

#### **Update Multiple Documents**

- **Increase the age of all users by 1 year:**
  ```js
  db.users.updateMany({}, { $inc: { age: 1 } });
  ```

---

#### **4. Deleting Data (DELETE)**

#### **Delete One Document**

- **Delete user Alice:**
  ```js
  db.users.deleteOne({ name: "Alice" });
  ```

#### **Delete Multiple Documents**

- **Delete all users older than 30:**
  ```js
  db.users.deleteMany({ age: { $gt: 30 } });
  ```

---

#### **4. Advanced Queries & Indexing**

#### **Sorting Results**

- **Sort users by age in descending order:**

  ```js
  db.users.find().sort({ age: -1 });
  ```

#### **Limiting Results**

- **Get only the first 5 users:**
  ```js
  db.users.find().limit(5);
  ```

#### **Indexing for Performance**

- **Create an index on the `email` field to speed up searches:**

  ```js
  db.users.createIndex({ email: 1 });
  ```
- **List all indexes:**

  ```js
  db.users.getIndexes();
  ```

---

#### **5. MongoDB Compass Features**

- **Visual Query Builder** → Easily build queries using UI.
- **Aggregation Pipeline** → Perform advanced data processing.
- **Schema Analysis** → Get insights into the database schema.
- **Index Management** → Improve performance by managing indexes.

------------------------------------------------------------------------------------
### Q004 : What is Sharding in DBMS;;

Sharding is a technique used in **DBMS (Database Management Systems)**
to **horizontally partition** data across multiple database servers.

It helps **scale out** a database by distributing the load across multiple
nodes instead of relying on a single machine.

---

### **1. What is Sharding?**

Sharding is the process of **splitting a large database into smaller, more
manageable pieces called shards**. Each shard contains a subset of the
database’s data and operates independently.

**Example:**

Imagine a user database with **1 billion users**.

Instead of storing them in a single database, we can split them into **10
shards**, each containing **100 million users**.

#### **Types of Database Scaling**

- **Vertical Scaling (Scaling Up)** → Adding more CPU, RAM, or Disk to a
  single server.
- **Horizontal Scaling (Scaling Out)** → Distributing data across multiple
  machines.
- **Sharding** is a **horizontal scaling technique**.

---

#### **2. Why Do We Need Sharding?**

#### **Problems with Single Large Databases**

- **Performance Bottlenecks** → Too many read/write operations slow down the
  system.
- **Storage Limitations** → A single server has limited disk space.
- **Scalability Issues** → Vertical scaling is expensive and has physical
  limits.
- **Single Point of Failure** → If one database crashes, the whole system goes
  down.

#### **How Sharding Solves These Issues?**

- **Increases Read/Write Throughput** → Queries are distributed across
  multiple nodes.
- **Reduces Storage Load** → Data is split, so each shard handles less data.
- **Improves Fault Tolerance** → If one shard fails, only part of the database
  is affected.
- **Supports Massive Scalability** → New shards can be added easily.

---

#### **3. Types of Sharding**

Sharding strategies determine how data is distributed across shards.

#### **1. Range-Based Sharding**

- **Data is divided based on a continuous range of values.**
- Example: **Users with IDs 1-1M in Shard 1, 1M-2M in Shard 2, etc.**
- **Pros:** Simple, easy to implement.
- **Cons:** Can cause **hotspots** (one shard may get more traffic than others).

```sql
-- Example: Storing users based on ID range
Shard1 → Users 1 to 1000000
Shard2 → Users 1000001 to 2000000
Shard3 → Users 2000001 to 3000000
```
---

#### **2. Hash-Based Sharding**

- **Data is distributed using a hash function** to ensure even distribution.

- Example: `Shard = hash(user_id) % total_shards`
  - **Pros:** Avoids hotspots, evenly distributes data.
  - **Cons:** Difficult to range-query data.

```python
def get_shard(user_id, total_shards):
    return hash(user_id) % total_shards
```
---

#### **3. Directory-Based Sharding**

- A **lookup table (directory)** keeps track of which shard stores which
  data.
- Example:

```json
{
  "UserID_1": "Shard1",
  "UserID_2": "Shard2",
  "UserID_3": "Shard1"
}
```
- **Pros:** Most flexible, supports dynamic sharding.
- **Cons:** Single point of failure if the directory is lost.

---

#### **4. Geo-Based Sharding (Location-Based)**

- Data is sharded **based on user location** (e.g., country or region).
- Example:
- **Shard 1 → Users from North America**
- **Shard 2 → Users from Europe**
- **Pros:** Great for localized applications like **Uber, Google Maps**.
- **Cons:** Uneven distribution if one region has more users than another.

---

#### **4. Sharding vs Replication**

| Feature      | Sharding                                | Replication                                         |
| ------------ | --------------------------------------- | --------------------------------------------------- |
| **Goal**     | Distribute data across multiple servers | Copy data across multiple servers                   |
| **Scaling**  | Horizontal scaling                      | Improves read performance but not write performance |
| **Storage**  | Data is divided across shards           | All nodes store the same data                       |
| **Use Case** | Large datasets, high write workloads    | High availability, read-heavy workloads             |
| **Example**  | Large e-commerce platforms like Amazon  | Backup copies for failover in banking systems       |

---

#### **5. Challenges of Sharding**

Even though sharding is powerful, it comes with challenges.

- **Complexity** → Setting up and managing shards is difficult.
- **Data Rebalancing** → If a shard gets too large, it needs to be split or moved.
- **Joins are Harder** → Joining data across shards requires additional processing.
- **Increased Latency** → Some queries may need to fetch data from multiple shards.
- **Single Point of Failure (Directory Sharding)** → If lookup tables fail, the system crashes.

---

#### **6. Real-World Use Cases of Sharding**

- **E-commerce** (Amazon, Flipkart) → Handling millions of products and
  transactions.
- **Social Media** (Facebook, Twitter) → Distributing user profiles, posts,
  and comments.
- **Banking Systems** → Partitioning customer accounts and transactions.
- **Streaming Platforms** (Netflix, YouTube) → Storing video metadata and
  watch history.
- **IoT & Big Data** → Handling millions of sensor data points in real-time.

---

#### **7. How to Implement Sharding in MongoDB?**

MongoDB has **built-in support for sharding**.

#### **Step 1: Enable Sharding on the Database**

```sh
sh.enableSharding("my_database")
```

#### **Step 2: Choose a Shard Key**

```sh
sh.shardCollection("my_database.users", { "user_id": "hashed" })
```

#### **Step 3: Add More Shards**

```sh
sh.addShard("shard1.example.com:27017")
sh.addShard("shard2.example.com:27017")
```
---

#### Q003 : MongoDB System Design Considerations

#### Pros of MongoDB in System Design

- Flexible Schema → No need to define a schema upfront.
- Horizontal Scalability (Sharding) → Distributes data across multiple
  machines.
- High Availability (Replication) → Multiple nodes store copies of data.
- Faster Reads/Writes → Optimized for high-speed operations.
- Built-in Aggregation Framework → Perform complex queries natively.

#### Cons of MongoDB in System Design

- Not ACID-Compliant by Default → Transactions are not as strong as SQL.
- Memory Usage → Stores duplicate data (denormalization increases space).
- Complex Joins → Does not support traditional joins like SQL; workarounds
  needed.
- Indexing Overhead → Too many indexes can slow down writes.
- Sharding Complexity → Needs careful planning to avoid performance
  bottlenecks.

------------------------------------------------------------------------------------
### Q002 : MongoDB Core Architecture;;

MongoDB is built around the concept of **Documents & Collections**,
replacing **Tables & Rows** in SQL.

#### **Basic MongoDB Structure:**

```
# Basic Design:
Database → Collections → Documents
```
- A **Collection** is like a **table** in SQL.
- A **Document** is like a **row**, but stores data in a
  flexible **JSON-like** format.
- Example **MongoDB Document (JSON-like structure)**:

```
{
  "_id": ObjectId("5f1a77a2b42f7a1b9c8e4567"),
  "name": "Rey",
  "age": 28,
  "skills": ["Python", "Django", "MongoDB"],
  "address": {
    "city": "Bangalore",
    "country": "India"
  }
}
```

#### **Key MongoDB Components:**

- **Document :** The smallest unit of data (JSON-like object).
- **Collection :** A group of documents (like a SQL table).
- **Database :** A container for multiple collections.
- **BSON :** A binary JSON format that MongoDB uses for storage.
- **Index :** Speed up queries by indexing fields.
- **Shard :** A partition of the database for horizontal scaling.
- **Replica Set :** A group of MongoDB instances for high availability.


------------------------------------------------------------------------------------
### Q001 : Introduction to NoSql;;

MongoDB is a **NoSQL** database designed for high-performance,
high-availability, and easy scalability.

It stores data in **JSON-like documents** (BSON format), making it more
flexible than relational databases.

#### **Key Features:**

- **Schema-less** → No fixed structure; each document can have different fields.
- **Scalable** → Supports **sharding** (horizontal scaling) for massive datasets.
- **Replication** → Data redundancy via **replica sets** ensures availability.
- **Rich Query Language** → Supports indexing, aggregation, geospatial queries.
- **High Performance** → Optimized for read/write operations compared to SQL.

#### **When to Use MongoDB?**

**MongoDB is ideal for:**

- **Big Data & Real-time Analytics** (Log processing, IoT data, event tracking).
- **Content Management** (CMS, blogging platforms, product catalogs).
- **E-commerce Applications** (Flexible product schemas, fast performance).
- **IoT Applications** (Handling high-velocity data streams).

**Not ideal for:**

- Banking/Finance (needs strict ACID compliance).
- Applications with complex relationships (SQL databases handle joins better).

---
