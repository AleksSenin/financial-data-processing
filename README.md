# Finance Analyzer

Finance Analyzer is a comprehensive solution for collecting, processing, storing, analyzing, and visualizing financial data.

## 📌 Description

This project collects data from financial APIs, processes it in real time using Kafka and Spark, stores it in databases (Cassandra and PostgreSQL), analyzes it using machine learning, and provides a user-friendly web interface for data visualization.

---

## ⚙️ Installation and Running the Project

### 🔹 1. Install Required Dependencies

Before running the project, make sure you have installed:
- **Docker** and **Docker Compose** ([Install Docker](https://docs.docker.com/get-docker/))
- **Python 3.10+** ([Download Python](https://www.python.org/downloads/))
- **Git** ([Install Git](https://git-scm.com/downloads))

### 🔹 2. Clone the Repository
```bash
 git clone https://github.com/your_username/financial-data-processing.git
 cd finance-analyzer
```

### 🔹 3. Start Docker Containers
```bash
 docker-compose up --build
```
This process will launch all services, including Kafka, Spark, databases, and the web interface for visualization.

### 🔹 4. Check if Everything is Running
After successful startup, open your browser and go to:
```
http://localhost:5000
```
Here, you can view financial data analytics and graphs.

---

## 📂 Project Structure

```
financial-data-processing/
│
├── ingestion_service/             # Collects data from APIs (Alpha Vantage, Yahoo Finance)
│   ├── data_collector.py         # Data collection logic
│   └── requirements.txt          # Dependencies
│
├── processing_service/           # Real-time data processing
│   ├── real_time_processing.py   # Uses Apache Kafka and Spark
│   └── requirements.txt          # Dependencies
│
├── storage_service/              # Data storage
│   ├── cassandra_connector.py    # Works with Cassandra
│   ├── postgresql_connector.py   # Works with PostgreSQL
│   └── requirements.txt          # Dependencies
│
├── analysis_service/             # Data analysis (machine learning)
│   ├── machine_learning.py       # Model training
│   └── requirements.txt          # Dependencies
│
├── visualization_service/        # Web interface for graphs and reports
│   ├── web_interface.py          # Flask + Plotly
│   └── requirements.txt          # Dependencies
│
├── docker-compose.yml            # Runs all services
├── README.md                     # Project documentation
└── requirements.txt               # General dependencies
```

---

## 📊 Project Components

### 1️⃣ Data Ingestion Service (Data Collection)
- Retrieves financial data via API (Alpha Vantage, Yahoo Finance)
- Formats and sends data to Kafka

### 2️⃣ Real-Time Processing Service (Data Processing)
- Uses Kafka + Spark Streaming for filtering and aggregating data

### 3️⃣ Data Storage Service (Data Storage)
- **Cassandra** for unstructured data
- **PostgreSQL** for structured data

### 4️⃣ Data Analysis Service (Data Analysis)
- Applies machine learning for stock price prediction
- Generates reports and insights based on historical data

### 5️⃣ Data Visualization Service (Data Visualization)
- Web interface (Flask + Plotly)
- Displays interactive stock price charts

---

## 🛠 Useful Commands

📌 **Stop Docker Services:**
```bash
 docker-compose down
```

📌 **Rebuild and Restart Services:**
```bash
 docker-compose up --build
```

📌 **Check Running Containers:**
```bash
 docker ps
```

📌 **Access a Container (e.g., PostgreSQL):**
```bash
 docker exec -it postgres_container_name psql -U username -d finance_db
```

---

## 🎯 Future Improvements

✅ Add support for new financial APIs
✅ Improve prediction algorithms using neural networks
✅ Expand the interface with customizable graphs

---

## 📢 Authors
- **[Aleksandr Senin]** – Project Developer
- **[GitHub Repository](https://github.com/AleksSenin/financial-data-processing.git)**


