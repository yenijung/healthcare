import pandas as pd
import numpy as np

df = pd.read_csv("data/insurance.csv")

df['smoker_binary'] = df['smoker'].map({'no': 0, 'yes': 1})

# interaction: smoker * BMI
df['smoker_bmi'] = df['smoker_binary'] * df['bmi']

# threshold: 1(BMI>=30)
df['bmi_30'] = (df['bmi'] >= 30).astype(int)

# smoker * threshold
df['smoker_bmi30'] = df['smoker_binary'] * df['bmi_30']

# smoker * age
df['smoker_age'] = df['smoker_binary'] * df['age']

# log(charges)
df['log_charges'] = np.log(df['charges'])

# bmi centered
df['bmi_centered'] = df['bmi'] - df['bmi'].mean()

df.to_csv("data/insurance_updated.csv", index=False)