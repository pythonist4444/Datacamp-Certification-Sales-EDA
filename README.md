# 📊 Product Sales Strategy Analysis

This repository contains a practical data analysis project completed as part of the [DataCamp Data Analyst Certification](https://www.datacamp.com/certification). The project evaluates the performance of three different sales methods used to promote a new line of office stationery.

---

## 🧠 Objective

Pens and Printers tested the following sales strategies:
- 📩 **Email only**
- 📞 **Call only**
- 📬 **Email + Call**

The goal was to identify which method:
- Reached the most customers
- Generated the highest revenue
- Delivered the best value for effort invested

---

## 📁 Dataset

The dataset includes 15,000 customer records across the following columns:

| Column | Description |
|--------|-------------|
| `week` | Week since product launch (1–6) |
| `sales_method` | One of the three sales strategies |
| `customer_id` | Unique customer ID |
| `nb_sold` | Number of products sold |
| `revenue` | Revenue generated |
| `years_as_customer` | Customer loyalty in years |
| `nb_site_visits` | Website engagement in the last 6 months |
| `state` | U.S. state for shipment |

📎 **Source:** Provided by DataCamp (for certification use only)

---

## 🛠️ Analysis Process

### 1. **Data Validation & Cleaning**
- Cleaned inconsistent values in `sales_method`
- Imputed missing `revenue` values using group-wise mean per method
- Validated column ranges, types, and outliers

### 2. **Exploratory Data Analysis**
- Bar plots, histograms, line charts, boxplots, and heatmaps created using Python
- Explored trends across sales methods, weeks, customer engagement, and loyalty

### 3. **Business Metric**
> **Average Revenue per Customer (ARPC)**

| Sales Method     | ARPC ($) |
|------------------|----------|
| Call             | 47.60    |
| Email            | 97.13    |
| Email + Call     | 183.65   |

**Email + Call** emerged as the most profitable and efficient method.

---

## ✅ Recommendations

- 📈 **Prioritize Email + Call** for future campaigns
- 📬 **Use Email** as a low-effort baseline method
- 🔻 **Deprioritize Call-only** – high effort, low return
- 📊 Track **ARPC weekly** for each method
- 🎯 Focus on **new customers** (0–3 years) with **moderate site visits (20–26)**

---

## 📄 Files Included

- `product_sales.csv`: Raw dataset (if available)
- `product_sales_cleaned.csv`: Cleaned dataset used in analysis
- `visuals_and_report/`: Folder containing plots and figures used
- `Sales-Strategy-Analysis-Report.md`: Full markdown version of report
- `Sales-Strategy-Analysis-Report.pdf`: Final printable PDF report
- `Sales-Strategy-Analysis-Report.pptx`: Presentation deck

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/pythonist4444/Datacamp-Certification-Sales-EDA
```

2. Open the notebook or markdown report to explore the project:
```bash
jupyter notebook
```

---

## 📬 Contact

**Author:** Abdulafeez Fakorede 
**Email:** faccojr0@gmail.com  
**LinkedIn:** [linkedin.com/in/abdulafeezfakorede](https://www.linkedin.com/in/abdulafeezfakorede/)

---

> 💡 This project was created as part of a professional certification. All assets are for educational and portfolio purposes only.
