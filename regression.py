import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from seaborn import scatterplot, histplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("data/insurance_updated.csv")

var = df.columns
print(var)

# baseline regression
df_model = df.copy()

X_base = df_model[['age', 'bmi', 'smoker_binary']]
y = df_model['charges']

X_train, X_test, y_train, y_test = train_test_split(X_base, y, test_size=0.2, random_state=42)

model_base = LinearRegression()
model_base.fit(X_train, y_train)

y_pred_base = model_base.predict(X_test)

rmse_base = np.sqrt(mean_squared_error(y_test, y_pred_base))
r2_base = r2_score(y_test, y_pred_base)

print("Baseline RMSE:", rmse_base)
print("Baseline R2:", r2_base)

# engineered regression
X_eng = df_model[['age', 'bmi', 'smoker_binary',
                  'smoker_bmi', 'bmi_30', 'smoker_bmi30', 'smoker_age']]

X_train, X_test, y_train, y_test = train_test_split(X_eng, y, test_size=0.2, random_state=42)

model_eng = LinearRegression()
model_eng.fit(X_train, y_train)

y_pred_eng = model_eng.predict(X_test)

rmse_eng = np.sqrt(mean_squared_error(y_test, y_pred_eng))
r2_eng = r2_score(y_test, y_pred_eng)

print("Engineered RMSE:", rmse_eng)
print("Engineered R2:", r2_eng)

'''
Baseline RMSE: 5874.763304187488
Baseline R2: 0.7776932310583375
Engineered RMSE: 4412.198998945896
Engineered R2: 0.8746044504245709

-> RMSE: how wrong is the model on average
         In this case, RMSE is 4 digit as the unit of the output is gbp.
-> R2: what percentage of data variability did model account for
       In general, 0.8+ is ideal. (0<R2<1)

RMSE is lower and R2 is higher in engineered model, meaning lower error and higher explainability.
Therefore, feature engineering was worth it. 
'''

# actual charges & predicted charges
# premium is germane to the predicted charges.
df_model['predicted_cost'] = model_eng.predict(X_eng)
# residual = actual - predicted
# residual > 0: underprediction
# residual < 0: overprediction
# Especially check if it underpredicts high-cost case as this can lead to company loss!
df_model['residual'] = df_model['charges'] - df_model['predicted_cost']
df_model['abs_residual'] = abs(df_model['residual'])

print(df_model[['charges', 'predicted_cost', 'residual', 'abs_residual']].head())
### TODO: SAVE DF SEPARATELY WHEN MODEL IS CONFIRMED.

plt.figure(figsize=(7,5))
scatterplot(x=df_model['predicted_cost'], y=df_model['residual'])
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs Predicted Cost")
plt.xlabel("Predicted Cost")
plt.ylabel("Residual (Actual - Predicted)")
plt.show(block=False)

'''
There are a number of underpredicted cost of high-cost case.
Let's focus on x-axis (predicted cost).
It is more stable on high-predicted section.
Model has high explainability (high R2) but cannot capture tail risk perfectly.
'''

print("Check residual that is higher than 10k residual.")
high_residual = df_model[df_model['residual'] > 10000]  # 86 cases

# check the pattern
print(high_residual[['age', 'bmi', 'smoker_binary']].mean())

'''
age              39.116279  # not considered as old
bmi              30.886860  # obese
smoker_binary     0.139535  # mean of binary variable = proportion!

-> We have high residual = smoker + high BMI.
However, smoker is only 14% of the whole high residual cases.
This means that the most of the cases are "non-smokers" but still high charges.
-> The model couldn't capture the high-cost cases in non-smokers.
'''

# Then, investigate what causes these non-smokers have high charges.
# i.e many children, specific region, not enough variables, noise
print("average number of children: ", high_residual['children'].mean()) # 1.1627906976744187
print("frequencies by regions: ", high_residual['region'].value_counts())   # northeast 27, northwest 24, southest 22, southwest 13
# Seems like children, region are not the direct causes also. -> "unexplained risk"
# Therefore, when designing pricing, premium function must contain safety margin / buffer.

