import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "product_sales.csv")

df = pd.read_csv(file_path)

# Step 1: Data Cleaning and Validation

print("Initial DataFrame shape:", df.shape)
print("Basic Info:\n", df.info())
print("First few rows of the DataFrame:\n", df.head())
print("Summary Statistics:\n", df.describe())
print("Missing Values:\n", df.isnull().sum())
print("Duplicate Rows\n", df.duplicated().sum(), '\n')

#  Cleaning and validating every column one by one

# 1.1 Check if 'week' column is in the correct format and has no missing values
print('Week column shape:', df['week'].shape) # Check shape of column which should be (1500,) row count
print('Week datatype:' ,df['week'].dtype) # Check datatype counted as int64 which is the week number since product launch
print("Missing values:" ,df['week'].isnull().sum()) # Check for nulls
print("Unique values:",df['week'].unique()) # Check for unique values
print("Number of unique values:",df['week'].nunique()) # Check for number of unique values
print("Range of values:",f"min: {df['revenue'].min()}, max: {df['revenue'].max()}") # Check for range of values
print("Column cleaned and validated \n")


# 1.2 Check if 'sales_method' column is in the correct format, has no missing values and has 3 unique values
print('Sales Method column shape:', df['sales_method'].shape) # Check shape of column which should be (1500,) row count
print('Sales Method datatype:', df['sales_method'].dtype) # Check datatype
print("Missing Values:", df["sales_method"].isnull().sum()) # Check for nulls
print("Unique Values:", df['sales_method'].unique()) # Check for unique values
print("Number of Unique Values:", df['sales_method'].nunique()) # Check for number of unique values

# 1.2b Normalizing and standardizing 'sales_method' column
df['sales_method'] = df['sales_method'].str.title() # Normalize the sales method names to title case
print("Unique sales methods after normalization:", df['sales_method'].unique())  # Check unique sales methods after normalization
print("Number of unique sales methods after normalization:", df['sales_method'].nunique())  # Check number of unique sales methods after normalization

df['sales_method'] = df['sales_method'].replace({"Em + Call": "Email + Call"}) # Replace "Em + Call" with "Email + Call"
print("Unique sales methods after replacement:", df['sales_method'].unique())  # Check unique sales methods after replacement
print("Number of unique sales methods after replacement:", df['sales_method'].nunique())  # Check number of unique sales methods after replacement
print("Column cleaned and validated \n")


# 1.3 Check if 'customer_id' column is in the correct format, has no missing values and has 1500 unique values
print('Customer ID column shape:', df['customer_id'].shape) # Check shape of column which should be (1500,) row count
print('Customer ID datatype:', df['customer_id'].dtype) # Check datatype should be object
print("Missing Values:", df["customer_id"].isnull().sum()) # Check for nulls
print("Number of unique values:",df['customer_id'].nunique()) # Check for number of unique values
print("Column cleaned and validated \n")


# 1.4 Check if 'nb_sold' column is in the correct format and has no missing values
print('Number of items sold column shape:', df['nb_sold'].shape) # Check shape of column which should be (1500,) row count
print('Number of items sold datatype:', df['nb_sold'].dtype) # Check datatype should be int
print("Missing Values:", df["nb_sold"].isnull().sum()) # Check for nulls
print("Range of values:",f"min: {df['nb_sold'].min()}, max: {df['nb_sold'].max()}") # Check for range of values
print("Column cleaned and validated \n")


# 1.5 Check if 'revenue' column is in the correct format and has no missing values
print('Revenue column shape:', df['revenue'].shape) # Check shape of column which should be (1500,) row count
print('Revenue datatype:', df['revenue'].dtype) # Check datatype should be float
print("Missing Values:", df["revenue"].isnull().sum()) # Check for nulls
print("Range of values:",f"min: {df['revenue'].min()}, max: {df['revenue'].max()}") # Check for range of values

# 1.5b Handling missing values in revenue column
print("Missing values in 'revenue' before handling:", df['revenue'].isnull().sum())
df['revenue'] = df['revenue'].groupby(df['sales_method']).transform(lambda x: x.fillna(x.mean()))  # Fill missing values with mean for each sales method
print("Missing values in 'revenue' after handling:", df['revenue'].isnull().sum())
print("Column cleaned and validated \n")


# 1.6 Check if 'years_as_customer' column is in the correct format and has no missing values
print('Years as customer column shape:', df['years_as_customer'].shape) # Check shape of column which should be (1500,) row count
print('Years as customer datatype:', df['years_as_customer'].dtype) # Check datatype should be int
print("Missing Values:", df["years_as_customer"].isnull().sum()) # Check for nulls
print("Range of values:",f"min: {df['years_as_customer'].min()}, max: {df['years_as_customer'].max()}") # Check for range of values
print("Column cleaned and validated \n")


# 1.7 Check if 'nb_site_visits' column is in the correct format and has no missing values
print('Number of site visits column shape:', df['nb_site_visits'].shape) # Check shape of column which should be (1500,) row count
print('Number of site visits datatype:', df['nb_site_visits'].dtype) # Check datatype should be int
print("Missing Values:", df["nb_site_visits"].isnull().sum()) # Check for nulls
print("Range of values:",f"min: {df['nb_site_visits'].min()}, max: {df['nb_site_visits'].max()}") # Check for range of values
print("Column cleaned and validated \n")


# 1.8 Check if 'state' column is in the correct format and has no missing values
print('State column shape:', df['state'].shape) # Check shape of column which should be (1500,) row count
print('State datatype:', df['state'].dtype) # Check datatype should be object
print("Missing Values:", df["state"].isnull().sum()) # Check for nulls
print("Unique values:",df['state'].unique()) # Check for unique values
print("Number of unique values:",df['state'].nunique()) # Check for number of unique values
print("Column cleaned and validated \n")


# 1.9 Checking for outliers in the data
print(df[['revenue', 'nb_sold', 'years_as_customer', 'nb_site_visits']].describe())

# 1.9b Visualizing outliers using boxplots
plt.figure(figsize=(12, 6))
for i, col in enumerate(['revenue', 'nb_sold', 'years_as_customer', 'nb_site_visits']):
    plt.subplot(1, 4, i + 1)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()


# Step 2: Exploratory Data Analysis (EDA)

# 2.1 Distribution of revenue per customer
plt.figure(figsize=(8, 5))
plt.hist(df['revenue'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Revenue per Customer')
plt.xlabel('Revenue in USD')
plt.xticks(rotation=45)
plt.xlim(left=0)  # Set x-axis limit to start from 0
plt.ylabel('Number of Customers')
plt.axvline(df['revenue'].mean(), color='red', linestyle='dashed', linewidth=1, label=f"Mean Revenue: {df['revenue'].mean():.2f}")
plt.legend()
plt.tight_layout()
plt.show()

# 2.1 Distribution of sales methods
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='sales_method', order=df['sales_method'].value_counts().index)
plt.title('Distribution of Sales Methods')
plt.xticks(rotation=45)
plt.xlabel('Sales Method')
plt.ylabel('Count of Sales Methods')
plt.show()

# 2.2 Revenue distribution by sales method
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='sales_method', y='revenue', estimator=np.sum, palette='viridis')
average_revenue = df['revenue'].mean()
# Adding a horizontal line for average revenue
plt.axhline(y=average_revenue, color='red', linestyle='--', linewidth=2, label=f"Average Revenue: {average_revenue:.2f}")
plt.title('Total Revenue by Sales Method (With Average Line)')
plt.xticks(rotation=45, fontsize=12)
plt.xlabel('Sales Method', fontsize=14)
plt.ylabel('Total Revenue', fontsize=14)
plt.legend()
plt.tight_layout()  # Adjust layout to avoid overlapping
plt.show()


# 2.3 Revenue over time
plt.figure(figsize=(12,6))
sns.barplot(data=df, x='week', y='revenue', estimator=np.sum, palette='viridis')
plt.title('Revenue for Each Week Since Product Launch')
plt.xlabel('Week')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='week', y='revenue', estimator=np.sum, palette='viridis', marker='o')
plt.title('Revenue for Each Week Since Product Launch')
plt.xlabel('Week')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2.4 Revenue by sales method over time
revenue_by_week_method = df.groupby(['week', 'sales_method'])['revenue'].sum().reset_index()
plt.figure(figsize=(14, 8))
sns.lineplot(data=revenue_by_week_method, x='week', y='revenue', hue='sales_method', marker='o', palette='tab10')
plt.title('Weekly Revenue by Sales Method')
plt.xlabel('Week')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.legend(title='Sales Method')
plt.tight_layout()
plt.show()


# 2.5 Revenue by number of site visits
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='nb_site_visits', y='revenue', estimator=np.sum, palette='plasma')
plt.title('Total Revenue by Number of Site Visits')
plt.xlabel('Number of Site Visits')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2.6 Revenue by number of products sold
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='nb_sold', y='revenue', estimator=np.sum, palette='magma')
plt.title('Total Revenue by Number of Products Sold')
plt.xlabel('Number of Products Sold')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2.7 Revenue by years as customer
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='years_as_customer', y='revenue', estimator=np.sum, palette='plasma')
plt.title('Total Revenue by Years as Customer')
plt.xlabel('Years as Customer')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2.8 Revenue by top 10 state of shipment
plt.figure(figsize=(12, 6))
top_states = df['state'].value_counts().nlargest(10).index
sns.barplot(data=df[df['state'].isin(top_states)], x='state', y='revenue', estimator=np.sum, palette='mako', order=top_states)
plt.title('Total Revenue by Top 10 States of Shipment')
plt.xlabel('State of Shipment')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2.9 Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df[['revenue', 'nb_sold', 'years_as_customer', 'nb_site_visits']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Step 3: Define a Business Metric

# 3.1 Avergage Revenue per Customer (ARPC) by Sales Method
arpc_by_sales_method = df.groupby('sales_method')['revenue'].mean().reset_index()
arpc_by_sales_method['revenue'] = arpc_by_sales_method['revenue'].round(2)  # Format to 2 decimal places
arpc_by_sales_method = arpc_by_sales_method.sort_values(by='revenue')
print("Average Revenue per Customer by Sales Method:\n", arpc_by_sales_method)

# 3.2 Total Revenue
total_revenue = df['revenue'].sum()
print(f"Total Revenue: {total_revenue:,.2f}") 



# Export the cleaned DataFrame to a CSV file
df.to_csv('product_sales_cleaned.csv', index=False)

# Note: Uncomment the lines below if you want to export the EDA results to a CSV
# Export the EDA results to a CSV file
# eda_results = {
#     'Total Revenue': [total_revenue],
#     'Average Revenue per Customer': [df['revenue'].mean()],
#     'Average Revenue per Customer by Sales Method': arpc_by_sales_method.to_dict(orient='records')
# }
# eda_results_df = pd.DataFrame(eda_results)
# eda_results_df.to_csv('eda_results.csv', index=False)