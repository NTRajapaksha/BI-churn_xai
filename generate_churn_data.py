import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import shap
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

print("1. Downloading Telco Churn dataset...")
url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
df = pd.read_csv(url)

print("2. Preprocessing data...")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)

df_powerbi = df.copy()
df_features = df.drop(columns=['customerID'])
categorical_cols = df_features.select_dtypes(include=['object']).columns

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_features[col] = le.fit_transform(df_features[col])
    label_encoders[col] = le

X = df_features.drop(columns=['Churn'])
y = df_features['Churn']

print("3. Training Random Forest model (bypassing XGBoost bugs)...")
model = RandomForestClassifier(random_state=42, n_estimators=50, max_depth=5)
model.fit(X, y)

print("4. Generating predictions...")
predictions = model.predict_proba(X)[:, 1]
df_powerbi['ChurnProbability'] = predictions

print("5. Calculating SHAP values...")
# RandomForest works natively with SHAP without the JSON serialization bugs
explainer = shap.TreeExplainer(model)
# Handle different SHAP versions (list vs 3D array)
shap_vals = explainer.shap_values(X)
if isinstance(shap_vals, list):
    shap_values_class1 = shap_vals[1]
elif len(shap_vals.shape) == 3:
    shap_values_class1 = shap_vals[:, :, 1]
else:
    shap_values_class1 = shap_vals

print("6. Formatting explainability for Power BI...")
feature_names = X.columns.tolist()
top_risk_factors = []
top_risk_impacts = []

for i in range(len(shap_values_class1)):
    row_shap = shap_values_class1[i]
    top_indices = np.argsort(row_shap)[::-1] 
    top_feature_idx = top_indices[0]
    
    top_risk_factors.append(feature_names[top_feature_idx])
    top_risk_impacts.append(row_shap[top_feature_idx])

df_powerbi['Top_Risk_Factor'] = top_risk_factors
df_powerbi['Top_Risk_Factor_Impact'] = top_risk_impacts

output_file = 'telco_churn_predictions.csv'
df_powerbi.to_csv(output_file, index=False)
print(f"\n✅ Success! Saved {len(df_powerbi)} rows to '{output_file}'.")
print("You can now load this CSV into Power BI Desktop.")
