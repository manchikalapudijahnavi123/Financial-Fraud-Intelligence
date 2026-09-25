# 🛡️ Financial Fraud Intelligence System
An explainable financial fraud detection system using **Machine Learning, Graph Analysis, Data Structures, and Algorithms**.

## 📌 About the Project

Financial fraud is becoming more common as digital payments and online transactions increase. I built this project to understand how different techniques can be combined to identify suspicious transactions.

The system takes transaction details such as **amount, location, device, merchant, and transaction activity** and analyzes them using different fraud detection methods.

It then generates a **risk score** and explains why a transaction may be considered suspicious.

The main goal of this project is to combine the **Data Structures, Algorithms, Machine Learning, and Backend Development** concepts I learned into one practical application.

## 🚀 What This Project Does

The system analyzes a transaction and provides:

- Fraud prediction
- Risk score
- Risk level (LOW, MEDIUM, HIGH, or CRITICAL)
- ML-based probability
- Behavioral anomaly detection
- Graph-based fraud alerts
- Reasons behind the result
- Transaction prioritization
- Explainable risk assessment

## ✨ Features

- Rule-based fraud detection
- Behavioral anomaly detection
- Machine learning-based prediction
- Graph-based fraud detection
- Explainable risk scoring
- Real-time transaction analysis
- Transaction prioritization
- FastAPI backend
- Simple web-based frontend
- Synthetic transaction data generation

## 🧠 Data Structures and Algorithms Used

### Data Structures

- Queue
- Deque
- Hash Table
- Priority Queue
- Heap
- Graph

### Algorithms

- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Sorting
- Hashing
- Sliding Window
- Cycle Detection

These concepts are used for processing transactions, identifying suspicious activity, prioritizing risky transactions, and investigating relationships between accounts, devices, merchants, and receivers.

## 🔍 How Fraud Detection Works

```text
Transaction Details
        ↓
Feature Extraction
        ↓
Rule Checking
        ↓
Behavior Analysis
        ↓
Machine Learning
        ↓
Anomaly Detection
        ↓
Graph Analysis
        ↓
Risk Score
        ↓
Risk Classification
        ↓
Final Result
```

The system combines multiple signals instead of depending on a single rule.

## 🤖 Machine Learning

The project uses an **online Logistic Regression model** to estimate the probability of fraudulent behavior.

The machine learning component works together with the other detection methods instead of being used alone.

The training and transaction data used in this project are **synthetic** and are mainly intended for learning and demonstration.

## 🕸️ Graph-Based Detection

Transactions can have relationships between different accounts, devices, merchants, and receivers.

I used a graph to represent these relationships and applied algorithms such as:

- BFS
- DFS
- Cycle Detection

These techniques help investigate suspicious connections within the transaction network.

## ⚠️ Risk Levels

| Risk Level | Meaning |
|------------|---------|
| LOW | Transaction appears normal |
| MEDIUM | Some suspicious activity is present |
| HIGH | Strong suspicious signals are detected |
| CRITICAL | Very high-risk transaction |

The result also includes the reasons that contributed to the risk classification.

## 🛠️ Technologies Used

### Backend

- Python
- FastAPI
- Pydantic

### Data Processing and Analysis

- NumPy
- Pandas
- Matplotlib

### Machine Learning

- Logistic Regression
- Online learning approach

### Frontend

- HTML
- CSS
- JavaScript

## 📁 Project Structure

```text
financial-fraud-intelligence/
│
├── backend/
│   ├── main.py
│   └── fraud_engine.py
│
├── frontend/
│   └── index.html
│
├── README.md
├── requirements.txt
└── .gitignore
```

## ▶️ How to Run

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Start the backend

Open the `backend` folder and run:

```bash
uvicorn main:app --reload
```

### 3. Open the website

Open `frontend/index.html` in a browser.

Make sure the FastAPI server is running while using the frontend.

## 🌐 FastAPI API

### Home

```text
GET /
```

Returns the backend status.

### Health Check

```text
GET /health
```

Checks whether the fraud detection engine is running.

### Fraud Detection

```text
POST /detect-fraud
```

The endpoint accepts transaction information such as:

- Amount
- Location
- Device ID
- Merchant
- Transaction Type
- Receiver ID
- Account ID
- Transaction ID

The response includes:

- Fraud prediction
- Fraud probability
- Risk score
- Risk level
- Rule score
- ML probability
- Anomaly status
- Graph alert
- Reasons
- Transaction features

## 📍 Transaction Locations

The system can work with different transaction locations, including locations such as:

- Guntur
- Hyderabad
- Vijayawada
- Bengaluru
- Chennai
- Mumbai
- Other locations included in the synthetic transaction data

These locations are used for educational transaction-analysis scenarios and do not represent real financial transactions.

## 📊 Example Result

```text
Prediction: FRAUD SUSPECTED
Risk Score: 78.82 / 100
Risk Level: HIGH
ML Probability: 99.9%
Behavioral Anomaly: YES
Graph Alert: YES
```

The exact result can vary depending on the transaction and the generated synthetic data.

## 📈 Dashboard

The project includes a Matplotlib-based dashboard that provides information such as:

- Total transactions
- High/Critical transactions
- Suspicious transaction rate
- Risk distribution
- Risk score trend

## 🕸️ Fraud Network Visualization

The project includes a graph visualization feature that creates a small network around a selected account using BFS-based graph traversal.

This demonstrates how graph algorithms can be applied to fraud investigation.

## 🔎 Transaction Explanation

The system can explain an individual transaction by displaying:

- Transaction ID
- Account
- Amount
- Location
- Device
- Time
- Risk Score
- Risk Level
- ML Probability
- Anomaly
- Graph Alert
- Reasons

This makes the system more explainable instead of only returning a fraud/not-fraud result.

## ⚡ Transaction Prioritization

A **Priority Queue** is used to prioritize transactions based on their risk scores.

Higher-risk transactions can be placed at the top of the queue so they can be examined first.

## 🗂️ Hash Table Lookup

A hash table is used to provide fast transaction lookup using the transaction ID.

```text
Transaction ID → Transaction Details
```

This demonstrates how hashing can be applied to efficiently access transaction information.

## 📚 What I Learned

While building this project, I got practical experience with:

- Applying DSA concepts to a real-world problem
- Building APIs using FastAPI
- Connecting a frontend with a backend
- Working with machine learning concepts
- Using graphs for fraud investigation
- Processing and analyzing transaction data
- Creating an explainable risk-scoring system
- Working with synthetic datasets
- Building an end-to-end software project

## 🔮 Future Improvements

Some things I would like to add in the future are:

- Database integration
- Better fraud prediction models
- Real-time notifications
- More detailed analytics
- Improved graph visualization
- Model performance evaluation
- User authentication
- Larger and more realistic synthetic datasets

## ⚠️ Disclaimer

This is a **student/educational project** built using synthetic transaction data.

It is not connected to real bank accounts, payment systems, or real financial data.

The fraud predictions and risk scores are intended only for **learning and demonstration purposes** and should not be used for actual financial decisions.

## 👩‍💻 Author

**Jahnavi Manchikalapudi**

B.Tech – Computer Science and Business Systems

## ⭐ Project Purpose

This project was created as a learning project to explore how **Data Structures, Algorithms, Machine Learning, Graph Analysis, and Backend Development** can be combined to build an explainable financial fraud detection system.
