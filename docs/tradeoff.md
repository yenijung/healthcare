# Trade-offs in Insurance Pricing

## Overview

Insurance pricing involves balancing multiple competing objectives.  
This project highlights the fundamental trade-offs between:

- Profitability  
- Risk management  
- Fairness  

No single pricing strategy can optimise all three simultaneously.

---

## 1. Profit vs Loss Reduction

### Observation

- Increasing margin significantly improves profit  
- However, loss ratio decreases only marginally  

### Interpretation

> Profit can be increased easily, but reducing loss cases is significantly harder.

---

### Why This Happens

- Margin scales predicted cost  
- But losses arise from prediction errors  

Therefore:

> Adjusting pricing does not fix incorrect predictions.

---

## 2. Prediction Accuracy vs Pricing Design

### Key Insight

> Pricing performance is driven more by prediction accuracy than pricing structure.

---

### Explanation

- If prediction is accurate → pricing works well  
- If prediction is wrong → all pricing strategies fail  

---

### Example

- predicted_cost = 14,000  
- actual cost = 30,000  

Even with higher margin:

- Premium remains far below actual cost  
- Loss persists  

---

## 3. Margin vs Safety Buffer

### Margin-Based Pricing

    Premium = predicted_cost × (1 + margin)

**Advantages:**

- Scales naturally with risk  
- Maintains proportional fairness  

**Limitations:**

- Ineffective against large prediction errors  
- Does not reduce loss cases significantly  

---

### Buffer-Based Pricing

    Premium = predicted_cost × (1 + margin) + buffer

**Advantages:**

- Reduces impact of underestimation  
- Improves stability  
- Lowers loss ratio  

**Limitations:**

- Applies uniformly to all individuals  
- Introduces fairness concerns  

---

### Key Trade-off

> Margin improves efficiency, while buffer improves robustness.

---

## 4. Efficiency vs Fairness

### Efficiency Perspective

- High-risk individuals pay more  
- Pricing aligns with expected cost  
- Profit is maximised  

---

### Fairness Perspective

- Low-risk individuals pay relatively more due to buffer  
- Cross-subsidisation occurs  
- Pricing is not perfectly aligned with actual cost  

---

### Core Conflict

> Improving financial stability often comes at the cost of fairness.

---

## 5. Cross-Subsidisation

The introduction of a safety buffer leads to:

- Redistribution of cost across individuals  
- Low-risk individuals partially covering high-cost cases  

---

### Interpretation

> Insurance inherently relies on risk pooling, but pricing adjustments can amplify or reduce this effect.

---

## 6. Structural Limitation

The most critical trade-off is:

> Prediction uncertainty vs pricing fairness

---

- To reduce losses → introduce buffer  
- To improve fairness → reduce buffer  

These objectives conflict directly.

---

## Final Insight

> There is no perfect pricing strategy — only different trade-offs between profitability, stability, and fairness.

---

## Conclusion

This project demonstrates that:

- Pricing strategies alone cannot solve the core problem  
- Prediction accuracy is the key driver of performance  
- Any improvement in robustness introduces fairness implications  

---

## Takeaway

> Effective insurance pricing is not about finding a perfect formula, but about managing trade-offs in an informed and transparent way.