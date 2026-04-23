'''
1. predicted cost를 기준으로 premium 만들기: premium = approximated x * (1 + margin)
2. 실제 비용과 비교해서 profit 계산: profit = premium - cost
3. 전체 profit 확인: total profit = sum(premium - cost) or average profit = 1/n * sum(premium - cost)
4. margin을 바꾸면서 simulation -> profit이 어떻게 변하는지, 누가 underpriced / overpriced 되는지
'''
import pandas as pd
from matplotlib import pyplot as plt

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

# loss case ratio
loss_ratio = (df_model['profit'] < 0).mean()
print("Loss ratio:", loss_ratio)    # around 0.09 -> stable as insurance pricing has pooling structure.

# profit per group
print(df_model.groupby('smoker')['profit'].mean())
print(df_model.groupby('bmi_30')['profit'].mean())

### result: The current pricing structure generates a disproportionate prop from the high-risk group!

# loss customer definition
loss_df = df_model[df_model['profit'] < 0].copy()
print("Number of loss customers: ", len(loss_df))
print("Loss ratio: ", len(loss_df) / len(df_model))

print("Loss group mean:")
print(loss_df[['age', 'bmi', 'predicted_cost', 'charges', 'profit']].mean())
print("\nOverall mean:")
print(df_model[['age', 'bmi', 'predicted_cost', 'charges', 'profit']].mean())
# result: actual doubled predicted. -> not about margin but model prediction error.

print("Loss rate by customer:")
print(loss_df['smoker'].value_counts(normalize=True))
print(df_model.groupby('smoker')['profit'].apply(lambda x: (x < 0).mean()))
print("Loss rate by BMI:")
print(df_model.groupby('bmi_30')['profit'].apply(lambda x: (x < 0).mean()))
# result: most of the losses are non-smoker cases. bmi shows not distinct differences.

print("Underpricing check:")
print(loss_df[['charges', 'predicted_cost', 'premium', 'profit']].head(10))
# result: charges (C) = 30k, predicted (C^)= 14k, premium = 16k, profit = -14k
# -> applying these values into the profit and premium formulas, this means it is model prediction accuracy problem not margin.

print("Check with residual:")
loss_df['residual'] = loss_df['charges'] - loss_df['predicted_cost']
print(loss_df['residual'].describe())
# result: mean residual: about 12300 whereas maximum residual: about 24300 -> too large

print("Check the high-cost section intensively:")
high_cost_loss = loss_df[loss_df['charges'] > 30000]
print("High-cost loss ratio:", len(high_cost_loss) / len(loss_df))
# result: ratio about 20%

## To conclude, models operate poorly with non-smoker high-cost prediction and unexpected medical cost.

### Then, how can we reduce loss without setting extremely unfair pricing?
## We have checked: The most of the loss is derived from non-smoker group. The cause is underestimation, which cannot be solved with margin.
## Therefore, the solution is "adding extra pricing on the group that are most likely to be underestimated".

## Three options:
# 1. Global margin (improve baseline): add extra price (fixed percentage) to everyone
# premium = predicted * (1 + m)
# However, this affects low-risk groups -> unfair
print("\n1. Global margin \n")
margins = [0.1, 0.2, 0.3]

for m in margins:
    df_model[f'premium_m_{int(m * 100)}'] = df_model['predicted_cost'] * (1 + m)
    df_model[f'profit_m_{int(m * 100)}'] = df_model[f'premium_m_{int(m * 100)}'] - df_model['charges']

    print(f"\nMargin {m * 100}%")
    print("Average profit:", df_model[f'profit_m_{int(m * 100)}'].mean())
    print("Loss ratio:", (df_model[f'profit_m_{int(m * 100)}'] < 0).mean())

# 2. Risk-based Margin: add extra price (fixed percentage) only to high-risk group
print("\n2. Risk-based margin \n")
margins = [0.1, 0.2, 0.3]
def risk_based_margin(row):
    if row['smoker'] == 'yes':
        return 0.20
    elif row['bmi'] >= 30:
        return 0.15
    else:
        return 0.10

df_model['margin_risk'] = df_model.apply(risk_based_margin, axis=1)

df_model['premium_risk'] = df_model['predicted_cost'] * (1 + df_model['margin_risk'])
df_model['profit_risk'] = df_model['premium_risk'] - df_model['charges']

print("Average profit:", df_model['profit_risk'].mean())
print("Loss ratio:", (df_model['profit_risk'] < 0).mean())

# 3. Safety Buffer: add extra price (fixed price) to everyone
# premium = predicted * (1 + m) + k
print("\n3. Safety bugger \n")
base_margin = 0.10
buffer = 2000

df_model['premium_buffer'] = df_model['predicted_cost'] * (1 + base_margin) + buffer
df_model['profit_buffer'] = df_model['premium_buffer'] - df_model['charges']

print("Average profit:", df_model['profit_buffer'].mean())
print("Loss ratio:", (df_model['profit_buffer'] < 0).mean())

## Conclusion: The profit increases as it goes up, but the loss ratio hardly decreases.
# However, "safety buffer" has the most profit with the least loss ratio.

### Then how much is the best buffer?
print("\nBuffer finalisation \n")

buffers = [1000, 2000, 3000, 4000]

for k in buffers:
    premium = df_model['predicted_cost'] * 1.1 + k
    profit = premium - df_model['charges']

    print(f"\nBuffer {k}")
    print("Average profit:", profit.mean())
    print("Loss ratio:", (profit < 0).mean())

# As one would expect, as the margin increases, profits rise and losses decrease.

# figures for README.md
# 1. Residual Plot
df_model['residual'] = df_model['charges'] - df_model['predicted_cost']

plt.figure(figsize=(7, 5))
plt.scatter(df_model['predicted_cost'], df_model['residual'], alpha=0.6)
plt.axhline(0, linestyle='--')
plt.xlabel("Predicted Cost")
plt.ylabel("Residual (Actual - Predicted)")
plt.title("Prediction Error: Residual Plot")
plt.tight_layout()
plt.savefig("figures/residual_plot.png", dpi=300)
plt.close()

# 2. Profit Distribution
plt.figure(figsize=(7, 5))
plt.hist(df_model['profit_buffer'], bins=40)
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.title("Profit Distribution under Safety Buffer Pricing")
plt.tight_layout()
plt.savefig("figures/profit_distribution.png", dpi=300)
plt.close()

# 3. Global Margin Analysis
margin_values = [0.10, 0.20, 0.30]
margin_avg_profits = []
margin_loss_ratios = []

for m in margin_values:
    premium = df_model['predicted_cost'] * (1 + m)
    profit = premium - df_model['charges']
    margin_avg_profits.append(profit.mean())
    margin_loss_ratios.append((profit < 0).mean())

plt.figure(figsize=(7, 5))
plt.plot([m * 100 for m in margin_values], margin_avg_profits, marker='o')
plt.xlabel("Global Margin (%)")
plt.ylabel("Average Profit")
plt.title("Average Profit by Global Margin")
plt.tight_layout()
plt.savefig("figures/global_margin_profit.png", dpi=300)
plt.close()

plt.figure(figsize=(7, 5))
plt.plot([m * 100 for m in margin_values], margin_loss_ratios, marker='o')
plt.xlabel("Global Margin (%)")
plt.ylabel("Loss Ratio")
plt.title("Loss Ratio by Global Margin")
plt.tight_layout()
plt.savefig("figures/global_margin_loss_ratio.png", dpi=300)
plt.close()

# 4. Buffer Sensitivity Analysis
buffer_values = [1000, 2000, 3000, 4000]
buffer_avg_profits = []
buffer_loss_ratios = []

for k in buffer_values:
    premium = df_model['predicted_cost'] * 1.10 + k
    profit = premium - df_model['charges']
    buffer_avg_profits.append(profit.mean())
    buffer_loss_ratios.append((profit < 0).mean())

plt.figure(figsize=(7, 5))
plt.plot(buffer_values, buffer_avg_profits, marker='o')
plt.xlabel("Safety Buffer")
plt.ylabel("Average Profit")
plt.title("Average Profit by Safety Buffer")
plt.tight_layout()
plt.savefig("figures/buffer_profit.png", dpi=300)
plt.close()

plt.figure(figsize=(7, 5))
plt.plot(buffer_values, buffer_loss_ratios, marker='o')
plt.xlabel("Safety Buffer")
plt.ylabel("Loss Ratio")
plt.title("Loss Ratio by Safety Buffer")
plt.tight_layout()
plt.savefig("figures/buffer_loss_ratio.png", dpi=300)
plt.close()

# 5. Strategy Comparison
strategy_names = ["Global 10%", "Global 20%", "Global 30%", "Risk-based", "Buffer"]
strategy_avg_profits = [
    df_model['profit_m_10'].mean(),
    df_model['profit_m_20'].mean(),
    df_model['profit_m_30'].mean(),
    df_model['profit_risk'].mean(),
    df_model['profit_buffer'].mean()
]

strategy_loss_ratios = [
    (df_model['profit_m_10'] < 0).mean(),
    (df_model['profit_m_20'] < 0).mean(),
    (df_model['profit_m_30'] < 0).mean(),
    (df_model['profit_risk'] < 0).mean(),
    (df_model['profit_buffer'] < 0).mean()
]

plt.figure(figsize=(8, 5))
plt.bar(strategy_names, strategy_avg_profits)
plt.xlabel("Pricing Strategy")
plt.ylabel("Average Profit")
plt.title("Average Profit by Pricing Strategy")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("figures/strategy_profit_comparison.png", dpi=300)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(strategy_names, strategy_loss_ratios)
plt.xlabel("Pricing Strategy")
plt.ylabel("Loss Ratio")
plt.title("Loss Ratio by Pricing Strategy")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("figures/strategy_loss_comparison.png", dpi=300)
plt.close()

print("Figures saved to results/figures/")