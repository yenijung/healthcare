import pandas as pd
import numpy as np
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