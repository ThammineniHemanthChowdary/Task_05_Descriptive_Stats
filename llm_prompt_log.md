# LLM Prompt Log – Task 05: Cars Dataset

## Model Used:
ChatGPT 4o (July 2025)  
– Session Link: *[Optional if logged]*  
– Date: July 29, 2025  

---

### 🔹 Prompt #1  
**Question:**  
> Which car in the dataset has the highest horsepower?

**LLM Response:**  
> The car with the highest horsepower in your dataset is the **Nissan Urvan**, with a horsepower of **2488.0**.

**Manual Validation:**  
✔️ Correct – Matches dataset numeric extraction.

**Commentary:**  
Prompt was direct, clean numeric parsing ensured accuracy.

---

### 🔹 Prompt #2  
**Question:**  
> What is the average top speed of all cars?

**LLM Response:**  
> The average top speed of all cars in the dataset is approximately **216.47 km/h**.

**Manual Validation:**  
✔️ Correct – Based on cleaned 'Total Speed' column.

**Commentary:**  
Basic aggregation handled correctly.

---

### 🔹 Prompt #3  
**Question:**  
> Which company sells the the most expensive model?

**LLM Response:**  
> The most expensive model is sold by **Bugatti**, and the car is the **La Voiture Noire**, priced at **$18,000,000**.

**Manual Validation:**  
✔️ Correct – Validated from max price row.

**Commentary:**  
Column cleaning on 'Cars Prices' helped ensure numeric comparison.

---

### 🔹 Prompt #4  
**Question:**  
> How many different fuel types are in the dataset?

**LLM Response:**  
> There are **23 different fuel types** in the dataset.

**Manual Validation:**  
✔️ Correct – Unique count on 'Fuel Types'.

**Commentary:**  
Handled via `nunique()`; straight and accurate.

---

### 🔹 Prompt #5  
**Question:**  
> What is the average acceleration time from 0 to 100 km/h?

**LLM Response:**  
> The average acceleration time from 0 to 100 km/h across all cars in the dataset is approximately **7.56 seconds**.

**Manual Validation:**  
✔️ Correct – Based on cleaned 'Performance(0 - 100 )KM/H' column.

**Commentary:**  
Numerical extraction enabled correct mean calculation.

---

### 🔹 Prompt #6  
**Question:**  
> Which fuel type offers the best average acceleration?

**LLM Response:**  
> *Plug-in hybrid* cars have the best (lowest) average acceleration time, around **2.5 seconds**.

**Manual Validation:**  
✔️ Correct – Based on fuel-type group averages.

**Commentary:**  
Correct use of grouped mean. Low value interpreted properly.

---

### 🔹 Prompt #7  
**Question:**  
> Which price segment has the highest average horsepower?

**LLM Response:**  
> The **Ultra Luxury** segment (cars priced above $10 million) has the highest average horsepower, approximately **1500 HP**.

**Manual Validation:**  
✔️ Correct – Grouped aggregation confirmed.

**Commentary:**  
Categorical binning and sorting handled accurately.

---

### 🔹 Prompt #8  
**Question:**  
> Among luxury cars, which has the best performance index?

**LLM Response:**  
> The **Bugatti Bolide** stands out with the highest performance index (Horsepower ÷ Acceleration), scoring around **840.91**.

**Manual Validation:**  
✔️ Correct – Derived using a custom performance metric.

**Commentary:**  
New index formula applied effectively.

---

### 🔹 Prompt #9  
**Question:**  
> Do electric or petrol cars have better speed-to-price ratios?

**LLM Response:**  
> *Petrol* cars offer a better speed-to-price ratio on average (**0.005687**) compared to electric cars (**0.003538**).

**Manual Validation:**  
✔️ Correct – Group comparison validated.

**Commentary:**  
Formulaic comparison yielded clear insight.

---

### 🔹 Prompt #10  
**Question:**  
> Which car offers the best horsepower per dollar value?

**LLM Response:**  
> The **Nissan Urvan** delivers the best value, offering approximately **0.0889 horsepower per dollar**.

**Manual Validation:**  
✔️ Correct – Based on `HorsePower_clean / Price_clean`.

**Commentary:**  
Value metric calculated and sorted accurately.

---

### 🔹 Prompt #11  
**Question:**  
> If I want a car under $60,000 with great acceleration and 4+ seats, what should I choose?

**LLM Response:**  
> The **Tesla Model 3 Performance** is the top choice, priced at **$53,240**, accelerating from 0–100 km/h in just **3.1 seconds**, and offering **5 seats**.

**Manual Validation:**  
✔️ Correct – Filtering and sorting were applied properly.

**Commentary:**  
Multi-condition filter worked well and picked a sensible option.

---

### 🔹 Prompt #12  
**Question:**  
> What are the top 3 cars that balance speed, price, and acceleration?

**LLM Response:**  
> 1. **Tata Motors Tiago EV**  
> 2. **Tata Motors Tiago EV** (variant)  
> 3. **Ford Fiesta**  
> These models have the best combined score based on speed-to-price and acceleration efficiency.

**Manual Validation:**  
✔️ Correct – Custom composite metric used.

**Commentary:**  
Fair balance metric used: `(TopSpeed / Price) * (1 / Acceleration)`.

---

### 🔹 Prompt #13  
**Question:**  
> Which price category gives the most torque for the money?

**LLM Response:**  
> The **Budget** segment provides the best torque-for-money ratio, making it the most efficient category for torque value.

**Manual Validation:**  
✔️ Correct – Grouped torque-per-dollar calculation.

**Commentary:**  
Used grouped average based on cleaned torque values.

---

### 🔹 Prompt #14  
**Question:**  
> If I’m a performance enthusiast with a $100K budget, what car should I buy and why?

**LLM Response:**  
> The **GMC Hummer EV Pickup Edition 1** offers the best performance value in this range, with **1000 horsepower**, **3.0-second acceleration**, and a performance score of **333.33**.

**Manual Validation:**  
✔️ Correct – Performance score calculated and sorted correctly.

**Commentary:**  
Smart use of `Horsepower / Acceleration` as the metric.

---

### 🔹 Prompt #15  
**Question:**  
> Assuming I want to reduce acceleration time in my fleet, should I switch to petrol or hybrid cars?

**LLM Response:**  
> Based on average acceleration times, **hybrid cars** perform slightly better than petrol cars. So, switching to **hybrids** would be more effective.

**Manual Validation:**  
✔️ Correct – Grouped mean confirms hybrid advantage.

**Commentary:**  
Categorical comparison handled accurately.

---

### 🔹 Prompt #16  
**Question:**  
> Which company should focus on improving acceleration to stay competitive?

**LLM Response:**  
> **Volvo** has the highest average acceleration time (**17.11 seconds**), indicating it could benefit most from focusing on acceleration performance.

**Manual Validation:**  
✔️ Correct – Company-level average acceleration evaluated.

**Commentary:**  
Logical conclusion from sorted grouped values.

---

### 🔹 Prompt #17  
**Question:**  
> Which model is an outlier in terms of horsepower compared to others in its price segment?

**LLM Response:**  
> The **Nissan Urvan**, priced at **$28,000**, stands out as a major outlier in the *Lower-Mid* segment, delivering **2488 horsepower**, which is more than **18 standard deviations above the mean**.

**Manual Validation:**  
✔️ Correct – Z-score calculation confirms it as a strong outlier.

**Commentary:**  
Statistical outlier correctly identified with high z-score (>2).

---
