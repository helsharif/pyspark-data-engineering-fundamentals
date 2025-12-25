# PySpark Fundamentals & Practical Exercises

Learning-focused repository covering the **core foundations of PySpark**, with practical, industry-relevant exercises that reflect how data scientists and data engineers actually use Spark in real workflows.

This repo demonstrates hands-on experience with distributed data processing, Spark DataFrames, ETL, performance considerations, and applied analytics at scale.

Based on Zero-to-Mastery's Data Engineering BootCamp learning modules at: https://zerotomastery.io/courses/data-engineering-bootcamp/

---

## 🎯 Objectives

By the end of this learning repo, I aimed to:
- Understand Spark architecture & execution model
- Work confidently with **Spark DataFrames**
- Perform **ETL-style transformations** at scale
- Write **efficient, production‑minded PySpark code**
- Explore **basic ML & analytics workflows** with Spark
- Practice working with real-world style structured data

---

## 🧱 Topics Covered

✔️ Spark Sessions & Lazy Execution  
✔️ DataFrames: creation, schema, typing  
✔️ Reading / writing data (CSV, Parquet)  
✔️ Filtering, joins, aggregations  
✔️ Handling nulls & data cleaning  
✔️ UDFs vs native Spark functions  
✔️ Performance awareness & best practices  
✔️ Intro to Spark ML 

---

## 🗂️ Repository Structure

```
pyspark-learning/
│
├── notebooks/
│   ├── 01_spark_basics.ipynb
│   ├── 02_dataframes_core.ipynb
│   ├── 03_transformations_etl.ipynb
│   ├── 04_joins_groupby_analytics.ipynb
│   ├── 05_performance_best_practices.ipynb
│   └── 06_intro_spark_ml.ipynb
│
├── data/
│   └── sample_data.csv   (small practice dataset)
│
└── README.md
```

> Note: Notebooks intentionally emphasize clarity, explanation, and applied reasoning — not just code.

---

## ⚙️ Environment & Setup

This project was built using **Python 3.11 + PySpark** in a Conda environment.

Example setup:

```bash
conda create -n spark_env python=3.11
conda activate spark_env
pip install pyspark
pip install pandas numpy
```

Then start Jupyter:

```bash
jupyter lab
```

---

## ▶️ Running the Notebooks

1️⃣ Clone repository  
2️⃣ Start your Spark-enabled environment  
3️⃣ Open `/notebooks` in Jupyter / VS Code  
4️⃣ Run cells sequentially

---

## 📌 Why This Repo Exists

Hiring teams increasingly expect:
- Experience working with distributed compute tools
- Comfort with **big data workflows**
- Ability to build reliable pipelines — not just notebooks

This repo demonstrates **hands-on Spark capability**, problem‑solving, and familiarity with scalable analytics tools.

---

## 🧠 Notes & Learning Mindset

This is not meant to be “perfect”; it is a **learning lab**.  
I’ve intentionally included explanations, comments, and intermediate thinking throughout the notebooks.

---

## 🌟 Next Steps (Future Enhancements)

- Larger real dataset exploration (e.g., NYC Taxi, weather, etc.)
- Spark SQL
- More Spark ML examples
- Structured streaming exploration

---

## 🤝 Feedback Welcome

If you're a recruiter, data team lead, or engineer reviewing this — I’d love feedback!  
Always improving, always learning.

---

**Author:** Husayn El Sharif  
