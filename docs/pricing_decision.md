# Pricing Decision

## Objective

The goal of pricing is not only to maximise profit, but also to ensure stability by reducing loss cases while maintaining reasonable fairness across individuals.

---

## Baseline Pricing Approach

The initial pricing rule follows a standard insurance structure:

    Premium = predicted_cost × (1 + margin)

This approach assumes that the predicted cost accurately reflects the expected medical expenditure.

---

## Problem Identification

However, analysis revealed a critical issue:

- A significant number of customers generate negative profit (loss cases)  
- Losses persist even when margins increase  

### Key Observation

- Example case:
  
  charges = 30,000  
  predicted_cost = 14,000  
  premium ≈ 16,000  

  → profit = -14,000  

This indicates:

> The loss is caused by severe underestimation, not insufficient margin.

---

## Why Increasing Margin Fails

Global margin adjustments were tested:

- Margin ↑ → Profit ↑ (linear increase)  
- Margin ↑ → Loss ratio ↓ (very small change)  

This implies:

> Increasing margin uniformly does not address the root cause of losses.

### Reason

- Margin scales the prediction  
- But if prediction is fundamentally wrong, scaling does not fix it  

---

## Risk-Based Pricing Evaluation

A risk-based approach was also tested:

- Higher margins applied to:
  - Smokers  
  - High BMI individuals  

### Result

- Profit improved moderately  
- Loss ratio remained largely unchanged  

### Interpretation

> The model fails to identify certain high-cost individuals, especially within low-risk groups.

Thus:

> Risk-based pricing cannot correct unseen prediction errors.

---

## Safety Buffer Approach

To address prediction uncertainty, a safety buffer was introduced:

    Premium = predicted_cost × (1 + margin) + buffer

### Key Idea

- Add a fixed amount to all customers  
- Protect against extreme underestimation  

---

## Empirical Results

The buffer strategy showed:

- Increased average profit  
- Gradual reduction in loss ratio  
- Improved stability against high-cost outliers  

### Interpretation

> The buffer directly compensates for prediction uncertainty, unlike margin-based methods.

---

## Final Decision

The selected pricing rule is:

    Premium = predicted_cost × (1 + 0.10) + 2000

### Justification

- 10% margin ensures baseline profitability  
- £2000 buffer mitigates underestimation risk  
- Achieves the best balance between:
  - Profitability  
  - Loss reduction  
  - Simplicity  

---

## Trade-Off

While effective, the buffer introduces a trade-off:

- All customers pay an additional fixed amount  
- Low-risk individuals may be relatively overcharged  

This leads to:

> Cross-subsidisation across the population.

---

## Final Insight

> Pricing performance is constrained more by prediction accuracy than pricing design.

---

## Conclusion

The pricing decision demonstrates that:

- Losses are driven by prediction error, not pricing structure  
- Margin adjustments alone are insufficient  
- A safety buffer provides a practical and robust solution  

However, this comes at the cost of fairness, highlighting the inherent trade-off in insurance pricing systems.