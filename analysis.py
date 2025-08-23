import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#loading csv
df = pd.read_csv("superstore.csv",encoding = "latin-1")

#looking for first 5 rows
print(df.head())

#looking for last five rowa
print(df.tail())

#checking shape
print("Rows,cols",df.shape)

#col names
print("Columns",df.columns.tolist())

#missing values
print(df.isna().sum())

#clean column names
df = df.rename(columns={"è®°å½æ°": "Record_Count"})
print("Cleaned Columns:", df.columns.tolist())
print(df.columns)

#basic exploration
#Total sales and profit
print("Total Sales :",df["Sales"].sum)
print("Total profit:",df["Profit"].sum)

#average values
print("average sales:",df["Sales"].mean())
print("Average profit:",df["Profit"].mean())

#sales and profit by category
print("\nSales by category:\n",df.groupby("Category")["Sales"].sum())
print("\nProfit by category:\n",df.groupby("Category")["Profit"].sum())

#sales and profit by region
print("\nSales by Region:\n", df.groupby("Region")["Sales"].sum())
print("\nProfit by Region:\n", df.groupby("Region")["Profit"].sum())

#deep exploration
#top 10 customer by sales and profit
print("\nTop 10 Customer by Sales:\n",df.groupby("Customer.Name")["Sales"].sum().sort_values(ascending = False).head(10))
print("\nTop 10 Customer by Profit:\n",df.groupby("Customer.Name")["Profit"].sum().sort_values(ascending = False).head(10))

print("\nTop 10 Products by Sales:\n", 
      df.groupby("Product.Name")["Sales"].sum().sort_values(ascending=False).head(10))

print("\nTop 10 Products by Profit:\n", 
      df.groupby("Product.Name")["Profit"].sum().sort_values(ascending=False).head(10))

print("\nSales by Segment:\n", df.groupby("Segment")["Sales"].sum())
print("\nProfit by Segment:\n", df.groupby("Segment")["Profit"].sum())



category_sales = df.groupby("Category")["Sales"].sum()
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values, color="skyblue", label="Sales")
sns.barplot(x=category_profit.index, y=category_profit.values, color="orange", alpha=0.7, label="Profit")
plt.title("Sales vs Profit by Category")
plt.ylabel("Amount")
plt.legend()
plt.show()

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="viridis")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.show()


# Make sure Order.Date is datetime
df["Order.Date"] = pd.to_datetime(df["Order.Date"], errors="coerce")

# Group by year-month
monthly_sales = df.groupby(df["Order.Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month-Year")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df[["Sales", "Profit", "Discount", "Quantity", "Shipping.Cost"]].corr(),
            annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Discount", y="Profit", data=df, alpha=0.5)
plt.title("Profit vs Discount")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

subcategory_sales = df.groupby("Sub.Category")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,8))
plt.pie(subcategory_sales.values, labels=subcategory_sales.index, autopct="%1.1f%%", startangle=140)
plt.title("Top 10 Sub-Categories Sales Contribution")
plt.show()

