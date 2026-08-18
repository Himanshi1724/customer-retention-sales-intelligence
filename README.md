# 📊 Customer Retention Intelligence Platform

An interactive **Customer Retention & Sales Intelligence Platform** built with Python, Machine Learning, and Streamlit.

The project analyzes customer purchasing behavior using **RFM Analysis**, performs **customer segmentation with K-Means clustering**, and uses **Machine Learning** to predict whether a customer is likely to make a repeat purchase within the next **90 days**.

---

## 🚀 Project Overview

Customer retention is an important part of business growth. Instead of focusing only on acquiring new customers, businesses can use customer data to identify valuable customers, customers at risk of leaving, and customers who are likely to purchase again.

This project provides a simple interactive platform that helps businesses:

* Understand customer purchasing behavior
* Segment customers based on their characteristics
* Identify high-value and at-risk customers
* Predict repeat purchase probability
* Generate business recommendations for different customer segments

---

## 🎯 Key Features

### 1. 📋 Project Overview

Provides an overview of the project, its purpose, and the techniques used.

The platform highlights:

* Data Cleaning
* Exploratory Data Analysis
* Customer-Level Feature Engineering
* RFM Analysis
* K-Means Customer Segmentation
* 90-Day Repeat Purchase Prediction
* Machine Learning Model Comparison

---

### 2. 👥 Customer Segmentation

Customers are divided into four business-oriented segments:

* ⭐ **VIP Customers**
* 💎 **Loyal High-Value Customers**
* 🟢 **Regular Customers**
* ⚠️ **At-Risk Customers**

These segments can help businesses create more targeted marketing and retention strategies.

---

### 3. 🎯 Repeat Purchase Prediction

Users can enter customer RFM information:

* **Recency** – Number of days since the customer's last purchase
* **Frequency** – Number of purchases
* **Monetary Value** – Customer spending value

The application then predicts whether the customer is likely to make another purchase within the next **90 days**.

The application also displays:

* Repeat purchase probability
* Prediction result
* Retention potential
* Probability progress bar

---

### 4. 💼 Business Recommendations

The platform provides practical recommendations for different customer segments.

Examples include:

| Customer Segment              | Recommended Strategy                                       |
| ----------------------------- | ---------------------------------------------------------- |
| ⭐ VIP Customers               | Provide exclusive rewards and personalized offers          |
| 💎 Loyal High-Value Customers | Use loyalty programs and cross-selling opportunities       |
| 🟢 Regular Customers          | Encourage repeat purchases with targeted promotions        |
| ⚠️ At-Risk Customers          | Launch win-back campaigns and personalized discount offers |

---

## 🤖 Machine Learning

The project uses machine learning to predict customer repeat purchases.

The final model used in the application is:

**Logistic Regression**

The model achieved approximately:

### 🎯 Model Accuracy: 65.8%

> Model accuracy is based on the current train/test evaluation performed during the project. It should be interpreted as a project-level evaluation metric rather than a guarantee of real-world prediction performance.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Logistic Regression
* K-Means Clustering
* Train/Test Split
* Feature Scaling
* Classification Metrics

### Application

* Streamlit

### Development Tools

* Jupyter Notebook
* Visual Studio Code
* Git
* GitHub

---

## 📈 RFM Analysis

RFM stands for:

### Recency

How recently a customer made a purchase.

### Frequency

How frequently a customer makes purchases.

### Monetary Value

How much money a customer spends.

RFM analysis helps businesses understand customer value and purchasing behavior.

---

## 🔄 Project Workflow

```text
Raw Customer Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Customer-Level Feature Engineering
        ↓
RFM Analysis
        ↓
K-Means Customer Segmentation
        ↓
Train/Test Split
        ↓
Feature Scaling
        ↓
Machine Learning Model
        ↓
Repeat Purchase Prediction
        ↓
Business Recommendations
        ↓
Streamlit Dashboard
```

---

## 📊 Application Pages

The Streamlit application contains four main sections:

### 🏠 Project Overview

Provides an overview of the project and the techniques used.

### 👥 Customer Segmentation

Displays the customer segmentation approach and customer groups.

### 🎯 Repeat Purchase Prediction

Allows users to enter RFM values and receive a 90-day repeat purchase prediction.

### 💼 Business Recommendations

Provides actionable strategies for different customer segments.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/Himanshi1724/AI_Customer_Retention_Platform.git
```

Move into the project directory:

```bash
cd AI_Customer_Retention_Platform
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

Run:

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
AI_Customer_Retention_Platform/
│
├── app/
│   └── app.py
│
├── data/
│   └── customer_data.csv
│
├── notebooks/
│   └── customer_retention_analysis.ipynb
│
├── .gitignore
├── README.md
├── requirements.txt
└── ...
```

> File names may vary depending on the final project structure.

---

## 📌 Example Prediction

For example, a customer can be evaluated using:

```text
Recency: 30 days
Frequency: 5 purchases
Monetary Value: 1000
```

The application generates a repeat purchase probability and classifies the customer's retention potential.

For example:

```text
Repeat Purchase Probability: 74.38%

🟢 High retention potential
```

The displayed probability will change according to the customer information entered into the application.

---

## 📚 Skills Demonstrated

This project demonstrates practical experience with:

* Python programming
* Data preprocessing
* Exploratory Data Analysis
* Feature engineering
* RFM analysis
* Customer segmentation
* K-Means clustering
* Machine Learning
* Classification
* Model evaluation
* Streamlit application development
* Git and GitHub
* Building an end-to-end data science project

---

## 🔮 Future Improvements

Possible future improvements include:

* Improving model performance through additional feature engineering
* Hyperparameter tuning
* Testing additional classification algorithms
* Adding interactive visualizations
* Adding customer-level prediction history
* Adding downloadable prediction reports
* Connecting the application to a live database
* Adding automated model retraining
* Deploying the application online

---

## 👩‍💻 Author

**Himanshi**

This project was developed as a practical Machine Learning and Data Science project focused on customer retention and business intelligence.

---

## ⭐ Conclusion

The **Customer Retention Intelligence Platform** combines data analysis, customer segmentation, machine learning, and business recommendations into one interactive application.

It demonstrates how customer transaction data can be transformed into meaningful insights that support **customer retention and targeted business strategies**.



## 👩‍💻 Author

**Himanshi**

GitHub: **Himanshi1724**

This project was developed as a practical **Data Science and Machine Learning project** focused on customer retention, customer segmentation, and business intelligence.
