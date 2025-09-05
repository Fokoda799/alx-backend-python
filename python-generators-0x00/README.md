# 🔄 Python Generators & Data Streaming Project

## 📌 Overview
This project explores advanced usage of **Python generators** to handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations.

By leveraging Python’s `yield` keyword, you will implement generators that allow **iterative access to data**, enabling efficient resource management and improved performance in data-driven applications.

---

## 🎯 Learning Goals
- **Master Generators** → Write generator functions and expressions for lazy evaluation.  
- **Work with Big Data** → Stream and batch-process large datasets without memory overload.  
- **Simulate Real-time Systems** → Model live data feeds and incremental updates.  
- **Optimize Performance** → Use generators for aggregate computations (e.g., averages).  
- **Integrate with Databases** → Combine Python generators with SQL queries for dynamic data fetching.  

---

## ⚙️ Requirements
- Python **3.x**  
- MySQL or SQLite  
- Familiarity with:
  - `yield` and generator functions  
  - SQL queries and database schema design  
  - Git & GitHub basics  

---

## 📂 Tasks

### [Task 0 — Database Setup & Seeding](./0-seed.py)
**Goal:** Connect to MySQL server and create/connect database.  

**Key functions:**
```python
def connect_db() → connect to MySQL server
def create_database(connection) → create ALX_prodev if missing
def connect_to_prodev() → connect directly to ALX_prodev
def create_table(connection) → set up user_data table
def insert_data(connection, data) → load records from user_data.csv
```

---

### [Task 1 — Streaming Rows One by One](./0-stream_users.py)
**Goal:** Stream rows from an SQL database one at a time.  

**Key function:**
```python
def stream_users() → Fetch rows one by one from the `user_data` table
```

---

### [Task 2 — Batch Processing Large Data](./1-batch_processing.py)
**Goal:** Create a generator to fetch and process data in batches.  

**Requirements:**
- `stream_users_in_batches(batch_size)` → fetch rows in chunks  
- `batch_processing(batch_size)` → filter users over age 25  
- Use ≤ 3 loops total  
- Must use `yield`  

**Sample Output (batch of 50):**
```python
{'user_id': '00234e50...', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede...', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
```

---

### [Task 3 — Lazy Loading Paginated Data](./2-lazy_paginate.py)
**Goal:** Simulate fetching paginated data lazily.  

**Requirements:**
- Implement `lazy_paginate(page_size)`  
- Include `paginate_users(page_size, offset)` helper  
- Use only **one loop**  
- Must use `yield`  

**Usage Example:**
```python
for page in lazy_paginate(100):
    for user in page:
        print(user)
```

---

### [Task 4 — Memory-Efficient Aggregation](./4-stream_ages.py)
**Goal:** Use a generator to compute aggregates without loading everything into memory.  

**Requirements:**
- `stream_user_ages()` → yields user ages one by one  
- Another function computes **average age** using the generator  
- No more than 2 loops  
- Not allowed to use SQL `AVG`  

**Sample Output:**
```
Average age of users: 78.4
```

---

## 📦 Repo Structure
```
alx-backend-python/
└── python-generators-0x00/
    ├── 0-seed.py
    ├── 0-stream_users.py
    ├── 1-batch_processing.py
    ├── 2-lazy_paginate.py
    ├── 4-stream_ages.py
    └── user_data.csv
```

---

## 🛠️ Run Examples
```bash
# Run Task 0, 1, 2, 3
./main.py

# Run Task 4 (average age)
./4-stream_ages.py
```

