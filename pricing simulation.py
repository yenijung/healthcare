'''
1. predicted cost를 기준으로 premium 만들기: premium = approximated x * (1 + margin)
2. 실제 비용과 비교해서 profit 계산: profit = premium - cost
3. 전체 profit 확인: total profit = sum(premium - cost) or average profit = 1/n * sum(premium - cost)
4. margin을 바꾸면서 simulation -> profit이 어떻게 변하는지, 누가 underpriced / overpriced 되는지
'''
import pandas as pd

df_model = pd.read_csv("data/insurance_with_predictions.csv")

print(df_model.columns)

## simple pricing rule
# margin setting
margin = 0.10
# premium calculation
df_model['premium'] = df_model['predicted_cost'] * (1 + margin)
# profit calculation
df_model['profit'] = df_model['premium'] - df_model['charges']

# check
print("Average predicted cost:", df_model['predicted_cost'].mean())
print("Average premium:", df_model['premium'].mean())
print("Average actual cost:", df_model['charges'].mean())
print("Average profit:", df_model['profit'].mean())
print("Total profit:", df_model['profit'].sum())

# result: Overall profit but still need more details.