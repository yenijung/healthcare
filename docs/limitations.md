# Limitations

## Overview

While the proposed pricing framework demonstrates strong performance in terms of profitability and stability, it is subject to several important limitations. These limitations arise from both the data and the modelling approach.

---

## 1. Limited Feature Space

The model relies on a small set of observable features:

- Age  
- BMI  
- Smoking status  

### Issue

These variables do not fully capture an individual’s health condition or medical risk.

### Implication

> Important drivers of medical costs (e.g., chronic diseases, genetic factors, lifestyle details) are not included.

As a result:

- Certain high-cost individuals cannot be identified in advance  
- Prediction errors remain unavoidable  

---

## 2. Prediction Error and Uncertainty

The analysis shows that losses are primarily caused by underestimation:

- Some individuals incur costs far above predicted values  
- These cases are not explained by existing features  

### Implication

> The pricing model depends heavily on prediction accuracy, but the prediction itself is inherently uncertain.

Even with pricing adjustments:

- Severe underestimation cannot be fully corrected  

---

## 3. Static Pricing Framework

The pricing rule is fixed:

    Premium = predicted_cost × (1 + margin) + buffer

### Issue

- No adaptation over time  
- No feedback loop from observed outcomes  

### Implication

> The model does not learn from past errors or adjust premiums dynamically.

In real-world settings:

- Pricing is often updated periodically  
- Risk is reassessed continuously  

---

## 4. Uniform Safety Buffer

The safety buffer is applied equally to all individuals:

- Same fixed amount regardless of risk level  

### Issue

- Disproportionate impact on low-cost individuals  

### Implication

> The buffer introduces cross-subsidisation and may lead to fairness concerns.

---

## 5. Simplified Modelling Approach

The cost prediction model is relatively simple:

- Linear regression with engineered features  

### Issue

- Limited ability to capture complex relationships  
- May not model non-linear or hidden interactions effectively  

### Implication

> More advanced models (e.g., ensemble methods, neural networks) could potentially improve prediction accuracy.

---

## 6. Lack of External Validation

The model is evaluated only on a single dataset:

- No validation across different populations  
- No robustness testing across environments  

### Implication

> The results may not generalise to real-world insurance markets.

---

## 7. No Behavioural or Market Considerations

The framework focuses purely on pricing mechanics:

- Does not consider customer behaviour  
- Does not account for market competition  

### Implication

> In practice, pricing decisions are influenced by demand, retention, and competition.

---

## Overall Insight

> The primary limitation of the system is not the pricing strategy itself, but the quality and completeness of the underlying predictions.

---

## Conclusion

The proposed framework provides a strong foundation for insurance pricing, but:

- Prediction uncertainty remains a critical challenge  
- Fairness concerns arise from simplified assumptions  
- Real-world deployment would require richer data, adaptive models, and market-aware adjustments  

---

## Future Direction

Addressing these limitations would involve:

- Incorporating richer health-related features  
- Using more advanced predictive models  
- Introducing dynamic or adaptive pricing strategies  
- Integrating fairness-aware optimisation techniques  