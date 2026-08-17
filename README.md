AI-Powered Customer Retention & Sales Intelligence Platform
📌 About the Project

This project explores customer purchasing behavior using e-commerce transaction data from the Online Retail II dataset.

The goal is not just to analyze past sales, but also to understand customer behavior and predict whether a customer is likely to make another purchase within the next 90 days.

Through this project, I worked on the complete data science workflow—from cleaning raw data and exploring sales patterns to customer segmentation and machine learning.

🎯 The Problem

For an e-commerce business, retaining existing customers is just as important as finding new ones.

The main question this project tries to answer is:

Can we use a customer's previous purchasing behavior to predict whether they will return and make another purchase within the next 90 days?

Answering this question can help businesses identify valuable customers, understand customers who may not return, and create better retention strategies.

📊 Dataset

This project uses the Online Retail II dataset, which contains real transactional data from an online retail business.

The dataset includes information such as:

Invoice Number
Stock Code
Product Description
Quantity
Invoice Date
Unit Price
Customer ID
Country
🔄 Project Workflow

The project was completed in the following steps:

Data Cleaning
Exploratory Data Analysis
Feature Engineering
RFM Analysis
Customer Segmentation using K-Means
Creating a 90-day repeat purchase target
Time-based Train-Test Split
Training and comparing Machine Learning models
Model Evaluation
Business Insights and Recommendations
🧹 Data Cleaning

The raw dataset required several cleaning steps before analysis.

This included:

Handling missing values
Removing duplicate records
Removing cancelled transactions
Removing invalid quantities and prices
Creating a TotalAmount feature for transaction-level analysis
📈 Exploratory Data Analysis

EDA was used to better understand the sales data and customer purchasing patterns.

The analysis includes visualizations related to:

Sales trends
Products and purchasing behavior
Revenue patterns
Customer activity
Country-level insights

A total of 10 visualizations from the analysis are saved in the visuals/ folder.

👥 Customer Segmentation

To better understand different types of customers, I used RFM Analysis and K-Means Clustering.

RFM represents:

Recency – How recently a customer made a purchase
Frequency – How often a customer makes purchases
Monetary – How much a customer spends

Using these features, customers were grouped into different segments based on their purchasing behavior.

🤖 Machine Learning

The machine learning part of the project focuses on predicting whether a customer will make another purchase within the next 90 days.

The following classification models were trained and compared:

Logistic Regression
K-Nearest Neighbors (KNN)
Decision Tree

A time-based train-test split was used so that the model is evaluated in a way that better reflects a real-world prediction scenario and helps reduce data leakage.

📊 Model Evaluation

The models were evaluated using:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix

The results were compared to understand how well each model performed on the customer repeat-purchase prediction task.

💡 What This Project Can Help With

The insights from this project can help a business:

Identify valuable customers
Understand customer purchasing patterns
Identify customers who may not return
Support targeted retention strategies
Make more data-driven business decisions
🛠️ Tools and Technologies
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook
VS Code
GitHub
Streamlit
📁 Project Structure
AI-Customer-Retention-Sales-Intelligence/
│
├── app/              # Streamlit application
├── data/             # Dataset
├── models/           # Saved machine learning models
├── notebooks/        # Data analysis and machine learning notebooks
├── visuals/          # Project visualizations
├── README.md
└── requirements.txt
🚀 Future Improvements

Some possible improvements for the project include:

Experimenting with additional machine learning models
Improving feature engineering
Adding more interactive visualizations
Deploying the project as a Streamlit application
Adding AI-generated business insights and recommendations
👩‍💻 Author

Himanshi Yadav

This version sounds more like a real person explaining what they built, instead of a generic AI-generated project description. It is still professional enough for your GitHub portfolio.

i did not want that interviw told me that you didnot make it it is ai genrated

Ahh, I understand you now. You don't want the README to sound so polished that an interviewer thinks you simply generated it with AI.

And honestly, that's a valid concern.

The best approach is not to hide AI use. Instead, the README should be simple and match the work you actually did. In an interview, you should be able to explain every section, every graph, and every model.

For example, instead of:

“This project leverages machine learning to generate actionable insights...”

Use simple language:

“In this project, I analyzed customer purchase data, created RFM features, segmented customers using K-Means, and built models to predict whether a customer would purchase again within 90 days.”

That sounds more natural because it directly describes your actual work.

Also, if an interviewer asks about it, the important thing is that you can explain:

Why you cleaned the data
Why duplicates were handled
What RFM means
Why you used K-Means
How the 90-day target was created
Why you used a time-based train/test split
Which models you tried and why
What your accuracy/results mean

You did work through these steps yourself, code by code. I helped guide you, but you should understand and be able to explain the project.

So let's make the README shorter, simpler, and based only on exactly what is actually in your project. We should not add impressive-sounding things that you cannot demonstrate.

now give me

Yes. Paste this simple, natural README into your README.md. It describes the work you actually did and avoids overly fancy language.

AI-Powered Customer Retention & Sales Intelligence Platform
About the Project

In this project, I worked with the Online Retail II dataset to analyze customer purchasing behavior.

The project starts with cleaning the raw transaction data and exploring the dataset. After that, I created customer-level features, performed RFM analysis, and used K-Means clustering to group customers based on their purchasing behavior.

The main machine learning task is to predict whether a customer will make another purchase within the next 90 days.

Project Goal

The goal of this project is to answer this question:

Based on a customer's previous purchase behavior, can we predict whether they will purchase again within the next 90 days?

The project also helps understand different customer groups and their purchasing patterns.

Dataset

The project uses the Online Retail II dataset.

The dataset contains transaction information such as:

Invoice Number
Stock Code
Description
Quantity
Invoice Date
Unit Price
Customer ID
Country
What I Did
1. Data Cleaning

I cleaned the dataset by handling issues such as:

Missing values
Duplicate records
Cancelled transactions
Invalid quantities and prices

I also created a TotalAmount feature for sales analysis.

2. Exploratory Data Analysis

I explored the data to understand:

Sales patterns
Customer purchasing behavior
Products
Revenue
Countries

The important visualizations from the project are saved in the visuals folder.

3. Customer-Level Features

Transaction-level data was converted into customer-level data so that each customer could be analyzed based on their purchasing behavior.

4. RFM Analysis

I created three important customer features:

Recency – How recently a customer made a purchase
Frequency – How often a customer made purchases
Monetary – How much the customer spent
5. Customer Segmentation

I used K-Means clustering to group customers with similar purchasing behavior.

This helped identify different types of customers based on their RFM values.

6. Repeat Purchase Prediction

The machine learning task was to predict whether a customer would make another purchase within the next 90 days.

A time-based approach was used for the train-test split to make the prediction setup more realistic and help avoid data leakage.

7. Machine Learning Models

I trained and compared:

Logistic Regression
K-Nearest Neighbors (KNN)
Decision Tree
8. Model Evaluation

The models were evaluated using:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Tools Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook
VS Code
GitHub
Streamlit

Project Structure
AI-Customer-Retention-Sales-Intelligence/
│
├── app/
├── data/
├── models/
├── notebooks/
├── visuals/
├── README.md
└── requirements.txt
Key Learning

Through this project, I practiced working through a complete data science workflow, including data cleaning, exploratory data analysis, feature engineering, customer segmentation, machine learning, and model evaluation.

Author

Himanshi Yadav
