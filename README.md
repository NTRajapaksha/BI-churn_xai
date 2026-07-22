# Predictive Churn & Explainable AI (XAI) Dashboard

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📌 Project Overview
Data Science models often fail to deliver business value because their outputs (predictions) remain trapped in Jupyter Notebooks or static CSVs. This project bridges the gap between **Machine Learning** and **Business Intelligence** by creating an end-to-end pipeline that feeds churn predictions and **SHAP (Shapley Additive explanations)** values directly into a highly interactive Power BI dashboard.

The dashboard empowers non-technical marketing stakeholders to dynamically filter high-risk customers, simulate ROI, and drill down into the exact reasons *why* an individual customer is leaving.

## 🚀 Key Features
* **ML to BI Pipeline:** A Python script automates data preprocessing, trains a Random Forest classifier on the IBM Telco Churn dataset, calculates SHAP values for interpretability, and exports a BI-ready structured dataset.
* **Dynamic What-If Parameters:** Built using advanced DAX, allowing stakeholders to adjust the "Risk Threshold" (e.g., top 10% vs top 20% flight risks) using a slider. The entire dashboard recalculates At-Risk Revenue and ROI instantly.
* **Explainable AI (XAI) Drill-throughs:** Users can right-click any high-risk customer on the scatter plot and "teleport" to an Explainability page, where SHAP values reveal the specific factors driving that exact customer's churn risk.
* **Financial Impact Modeling:** Translates raw probabilities into business metrics (At-Risk Revenue, Retention ROI), proving the financial value of the ML model.

## 🏗️ Architecture & Tools
1. **Python (Scikit-Learn, SHAP, Pandas):** Model training, probability scoring, and feature importance extraction.
2. **Power BI Desktop:** Star Schema Data Modeling, DAX (Data Analysis Expressions), and modern UI/UX design (Dark Mode/Glassmorphism).

## 📂 Repository Structure
```text
├── generate_churn_data.py       # Python script to train model and generate SHAP CSV
├── telco_churn_predictions.csv  # The output bridging file
├── Churn_Dashboard.pbix         # The interactive Power BI dashboard file
└── README.md
```

---

## 🔍 Codebase Walkthrough: What Happens in Each File

### 1. The Machine Learning Engine
**`generate_churn_data.py`**
- **Purpose:** The brain of the operation. It handles data processing, model training, and AI explainability.
- **What it does:** 
  1. **Data Ingestion & Cleaning:** Downloads the dataset and handles missing values.
  2. **Model Training:** Trains a `RandomForestClassifier` on the historical data.
  3. **Prediction:** Calculates the `ChurnProbability` for every customer.
  4. **SHAP Integration:** Runs the model through a `TreeExplainer` to get the SHAP values. It extracts the strongest driving factor for churn for each customer as `Top_Risk_Factor` and `Top_Risk_Factor_Impact`.
  5. **Export:** Merges the original data, probabilities, and SHAP insights into `telco_churn_predictions.csv`.

### 2. The Business Intelligence Layer
**`Churn_Dashboard.pbix`**
- **Purpose:** The interactive visual interface for stakeholders.
- **What it does:** 
  - **Data Ingestion:** Loads the structured `telco_churn_predictions.csv`.
  - **What-If Scenarios:** Uses DAX (Data Analysis Expressions) to create interactive sliders, calculating ROI based on Risk Thresholds dynamically.
  - **Drill-Through Pages:** Utilizes Power BI's drill-through functionality, allowing a seamless transition from a macro-view of the customer base to a single customer's AI-generated risk profile.

---

## ⚙️ How to Run Locally

### 1. Generate the ML Data
Ensure you have the required Python libraries installed:
```bash
pip install pandas numpy scikit-learn shap
```
Run the Python script to fetch the dataset, train the model, and generate the CSV:
```bash
python generate_churn_data.py
```

### 2. View the Dashboard
1. Open `Churn_Dashboard.pbix` in **Power BI Desktop**.
2. If prompted, click **Refresh Data** to pull in the latest predictions from your local CSV.
3. Use the **Risk Threshold** slider on Page 1 to simulate different marketing interventions, and right-click a customer on the scatter plot to drill through to the AI Explainability page.

## 📈 Business Impact
By putting SHAP explainability directly into the hands of retention agents via a BI tool, this architecture reduces time-to-insight from days (waiting on data science reports) to milliseconds. It enables highly targeted, personalized retention campaigns based on individualized risk factors.
