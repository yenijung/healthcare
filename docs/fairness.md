# Fairness Analysis

## Objective

This section evaluates whether the proposed pricing strategy distributes costs fairly across different groups, and identifies any systematic imbalance in pricing outcomes.

---

## Definition of Fairness

In this project, fairness is assessed based on:

- **Pricing error** (premium − actual cost)  
- **Profit distribution across groups**  
- **Loss ratio across groups**  

The goal is to understand whether certain groups are consistently overcharged or underpriced.

---

## Group Analysis: Smoking Status

### Average Profit

| Group | Average Profit |
|------|---------------|
| Non-smoker | 2903 |
| Smoker | 5273 |

### Loss Ratio

| Group | Loss Ratio |
|------|-----------|
| Non-smoker | 0.093 |
| Smoker | 0.055 |

---

### Interpretation

- Smokers generate significantly higher profit  
- Non-smokers have a higher loss ratio  

This suggests:

> High-risk individuals are consistently charged more, while low-risk individuals are more likely to generate losses.

---

## Group Analysis: BMI

### Average Profit

| BMI Group | Average Profit |
|----------|---------------|
| BMI < 30 | 3056 |
| BMI ≥ 30 | 3685 |

### Loss Ratio

| BMI Group | Loss Ratio |
|----------|-----------|
| BMI < 30 | 0.082 |
| BMI ≥ 30 | 0.088 |

---

### Interpretation

- Higher BMI individuals generate slightly more profit  
- Loss ratios are similar across groups  

This indicates:

> BMI contributes to pricing differences but is not a dominant factor in fairness outcomes.

---

## Impact of Safety Buffer

The final pricing model includes a fixed buffer:

    Premium = predicted_cost × (1 + margin) + buffer

### Effect

- All individuals pay an additional fixed amount  
- The relative impact is larger for low-cost individuals  

---

### Implication

> The buffer redistributes financial burden across the population.

---

## Cross-Subsidisation

The analysis reveals a clear cross-subsidisation effect:

- High-risk individuals are systematically charged more  
- Low-risk individuals contribute to covering unexpected high-cost cases  

---

### Key Insight

> The pricing system pools risk across individuals, but does so unevenly.

---

## Source of Inequality

The main driver of unfairness is not pricing itself, but:

- Prediction error  
- Underestimation of certain high-cost individuals  

---

### Example

- predicted_cost = 14,000  
- actual cost = 30,000  

→ large loss regardless of pricing strategy  

---

## Overall Interpretation

The pricing model achieves:

- Strong profitability  
- Reduced loss frequency  

However, it introduces:

- Uneven profit distribution  
- Cross-subsidisation  
- Sensitivity to prediction error  

---

## Conclusion

> The pricing strategy is economically efficient but not fully fair.

It reflects a common trade-off in insurance systems:

- Improving stability and profitability  
- Requires accepting imbalances in how costs are distributed across individuals  

---

## Final Insight

> Fairness in pricing cannot be achieved without improving prediction accuracy.