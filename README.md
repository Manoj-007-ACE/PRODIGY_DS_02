# PRODIGY_DS_02 — Titanic Dataset EDA & Data Cleaning

## 📌 Task
Perform data cleaning and exploratory data analysis (EDA) 
on the Titanic dataset from Kaggle. Explore relationships 
between variables and identify patterns and trends.

## 🛠 Tools Used
Python | Pandas | Matplotlib | Seaborn | NumPy

## 🧹 Data Cleaning Steps
- Filled missing Age values with median (177 missing)
- Dropped Cabin column (687 missing — 77%!)
- Filled missing Embarked with mode (2 missing)
- Dropped irrelevant columns: PassengerId, Name, Ticket
- Encoded Sex column: male=0, female=1

## 📊 Key Findings
- Overall survival rate: 38.4%
- Female survival rate: 74.2% vs Male: 18.9%
- 1st class survival: 63% vs 3rd class: 24.2%
- Sex was strongest predictor (0.54 correlation)
- Higher fare = higher chance of survival

## 📈 Visualizations Created
- plot1_survival_count.png — Overall survival count
- plot2_survival_gender.png — Survival by gender
- plot3_survival_class.png — Survival by passenger class
- plot4_age_distribution.png — Age distribution by survival
- plot5_fare_class.png — Fare distribution by class
- plot6_heatmap.png — Correlation heatmap

## 📁 Files
- task2.py — Main code
- plot1_survival_count.png
- plot2_survival_gender.png
- plot3_survival_class.png
- plot4_age_distribution.png
- plot5_fare_class.png
- plot6_heatmap.png

## 🏢 Internship
Prodigy InfoTech Data Science Internship — Task 2
