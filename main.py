import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read sales data
df = pd.read_csv("sales_data.csv")

# Calculate total sale per row
df["TotalSale"] = df["Quantity"] * df["UnitPrice"]

# Total sales per product
product_sales = df.groupby("Product")["TotalSale"].sum().sort_values(ascending=False)
print("Total Sales per Product:")
for product, total in product_sales.items():
    print(f"{product}: €{total:.2f}")
print("\n")

# Total sales per category
category_sales = df.groupby("Category")["TotalSale"].sum()
print("Total Sales per Category:")
for category, total in category_sales.items():
    print(f"{category}: €{total:.2f}")
print("\n")

# Sales over time
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["TotalSale"].sum()

# Plot settings
sns.set_style("whitegrid")

# Bar chart: Product sales
plt.figure(figsize=(10,6))
product_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales per Product (€)")
plt.ylabel("Sales")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()

# Pie chart: Category sales
plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct='%1.1f%%', colors=["#ff9999","#66b3ff"])
plt.title("Total Sales per Category (€)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# Line chart: Daily sales
plt.figure(figsize=(10,6))
daily_sales.plot(marker="o", linestyle="-", color="green")
plt.title("Daily Sales (€)")
plt.ylabel("Sales")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_sales.png")
plt.show()

print("Analysis completed! Charts saved as PNG files.")