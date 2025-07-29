# 🧠 Task 05 – Descriptive Statistics with Large Language Models

## 📁 Dataset
- **Title:** Cars Datasets 2025  
- **Source:** Kaggle (https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025)  
- **Size:** ~1,200 rows × 11 columns  
- **Content:** Car specifications including company, model, engine capacity, horsepower, acceleration, top speed, price, fuel type, torque, and seating.

> ⚠️ Per instructions, the dataset file is **not included** in this repository. It resides locally under `data/`.

---

## 🎯 Objective
The goal of this research task was to:
1. Choose a small, public dataset.
2. Generate descriptive and strategic statistics using Python.
3. Use a large language model (LLM) such as ChatGPT to answer natural language questions about the dataset.
4. Validate the model’s answers against computed results.
5. Reflect on prompt engineering, LLM reasoning, and response accuracy.

---

## 🛠️ What I Did

### ✅ Step 1: Dataset Selection  
I selected the **Cars Datasets 2025** because it offered a clean, structured dataset with diverse attributes to support both factual and reasoning-based questions.
link: https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025?resource=download

### ✅ Step 2: Descriptive Statistics  
I wrote a Python script (`basic_stats.py`) that:
- Extracted numeric values from formatted strings.
- Calculated summary statistics:
  - Average horsepower, acceleration, price, engine size, and torque.
  - Top 5 performers by horsepower, acceleration, price.
- Generated grouped insights:
  - Horsepower and price by fuel type.
  - Acceleration by fuel type.
  - Horsepower by seat count.
- Computed advanced metrics like:
  - Horsepower-to-price ratio
  - Speed-to-acceleration ratio
  - Speed-to-price ratio

Results were saved to:
- `output/summary_stats.json`  
- `output/top_performers.txt`

### ✅ Step 3: Prompting the LLM  
Using **ChatGPT-4o**, I asked a series of natural language questions based on the dataset, such as:
- "Which car has the highest horsepower?"
- "What fuel type accelerates the fastest on average?"
- "If I want a car under $100,000 with high performance, which model should I consider?"

I logged:
- Each prompt
- The LLM’s response
- Whether it was correct, incorrect, or partially correct
- Notes on prompt refinement and LLM behavior

👉 See `llm_prompt_log.md` for full details.

---

## 📂 File Structure
```
Task_5/
├── data/ # Contains dataset (not uploaded to GitHub)
│ └── Cars Datasets 2025.csv
├── output/ # Auto-generated results
│ ├── summary_stats.json
│ └── top_performers.txt
├── basic_stats.py # Python script for stats generation
├── llm_prompt_log.md # Prompt/response log with validation
└── README.md # This file
```

---

## 🧪 Tools Used
- Python 3.13
- pandas, re, json, os
- ChatGPT (GPT-4o, July 2025)
- VS Code

---

## 🧠 Key Learnings
- LLMs like ChatGPT can interpret structured data and answer factual questions with high accuracy if the column names are clearly referenced.
- For strategic questions, such as recommendations under constraints (e.g., "best value car under 100K"), LLMs need clearly framed metrics and prompt guidance.
- Prompt phrasing and specificity significantly impacted LLM performance—minor changes often led to improved or corrected answers.

---
