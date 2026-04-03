# ATM Intelligence Demand Forecasting System

## 👨‍🎓 Student Details

* Name: Dwij Vala
* Student Code: 2505369
* Course: Artificial Intelligence (CRS)
* Assessment: FA-2 Data Mining

---

## 🌐 Live App

[Click here to view the app](https://atm-app-dwij.streamlit.app/)

---

## 📌 App Evidence

<img width="1919" height="924" alt="image" src="https://github.com/user-attachments/assets/e29692a6-750a-4102-9389-9d5c9bf645e0" />
<img width="1915" height="906" alt="image" src="https://github.com/user-attachments/assets/e611d47d-cc56-4b93-bac7-65b5e4ef7d56" />
<img width="1918" height="912" alt="image" src="https://github.com/user-attachments/assets/7341361f-6477-4197-bd19-8efe9d7fdcb3" />
<img width="1912" height="914" alt="image" src="https://github.com/user-attachments/assets/c2387dd5-7646-4771-a568-17df507f6246" />
<img width="1914" height="913" alt="image" src="https://github.com/user-attachments/assets/4717f1a8-8788-49c7-9502-8d42213af401" />
<img width="1917" height="919" alt="image" src="https://github.com/user-attachments/assets/d5fe70b0-6f00-4c3e-93d1-4df3bf4ac828" />
<img width="1916" height="915" alt="image" src="https://github.com/user-attachments/assets/25fd710c-e14c-407e-b9c9-8931a805628a" />
<img width="1919" height="919" alt="image" src="https://github.com/user-attachments/assets/eb3169da-45cd-49ec-be50-40d3bdf94d4f" />








---

## 📌 Project Overview

This project focuses on analyzing ATM transaction data to generate actionable insights for efficient cash management. It applies data mining techniques such as Exploratory Data Analysis (EDA), clustering, and anomaly detection to understand demand patterns and support decision-making.

---

## 🎯 Objectives

* Identify patterns and trends in ATM usage
* Group ATMs based on demand behavior
* Detect unusual spikes in withdrawals
* Build an interactive system for analysis

---

## 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset and uncover patterns:

* Distribution of withdrawals and deposits
* Time-based trends (daily and weekly)
* Impact of holidays and special events
* External factors such as weather and competition
* Relationship analysis using correlation and scatter plots

---

## 🤖 Clustering Analysis

K-Means clustering was applied to group ATMs into meaningful categories:

* High-demand ATMs (urban, event-heavy areas)
* Medium-demand ATMs (commercial/business zones)
* Low-demand ATMs (residential or rural areas)

The Elbow Method was used to determine the optimal number of clusters.

---

## 🚨 Anomaly Detection

Isolation Forest was used to detect anomalies in ATM withdrawals:

* Identifies unusual spikes in demand
* Highlights potential risks of cash shortage
* Detects abnormal behavior during holidays or events

---

## 🖥️ Interactive Streamlit Application

The project includes a fully interactive dashboard built using Streamlit:

* Filter data by:

  * Day of Week
  * Time of Day
  * Location Type

* Visualize:

  * Demand patterns
  * ATM clusters
  * Anomalies in transactions

---

## 📂 Project Structure

ATM-Demand-Forecasting/
│
├── app.py
├── eda_analysis.py
├── clustering_anomaly.py
├── atm_dataset.csv
├── requirements.txt
├── README.md

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd ATM-Demand-Forecasting
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows:

```bash
venv\Scripts\activate.bat
```

#### Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## 📊 Key Insights

* ATM demand shows significant fluctuations with spikes
* Weekends and evenings have higher withdrawal activity
* Holidays and events strongly influence cash demand
* Clustering helps optimize ATM cash distribution
* Anomalies highlight unusual transaction patterns

---

## 🧠 Learning Outcomes

* Applied EDA techniques to real-world data
* Implemented clustering using K-Means
* Performed anomaly detection using machine learning
* Built an interactive dashboard using Streamlit
* Transformed raw data into actionable insights

---

## 🚀 Future Improvements

* Real-time data integration
* Predictive modeling using machine learning
* Cloud deployment and scalability
* Enhanced UI/UX

---

## 📌 Conclusion

This project demonstrates how data mining techniques can be used to improve ATM cash management. By combining analysis, clustering, and anomaly detection, it provides a structured approach to understanding and optimizing ATM demand.

---
