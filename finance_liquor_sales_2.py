import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv")

# filter 2016 - 2019
df["date"] = pd.to_datetime(df["date"])
filtered_df = df[(df["date"].dt.year >= 2016) & (df["date"].dt.year <= 2019)].reset_index()

# find total sales
total_sales = sum(filtered_df["sale_dollars"])

# find sales per store
sales = filtered_df.groupby("store_name")["sale_dollars"].sum()

# find percentage sales
percentage_sales = (sales * 100 / total_sales).round(2)

# sort and print
percentage_sorted_sales = percentage_sales.sort_values(ascending=True).tail(15)
print(percentage_sorted_sales)

p = plt.barh(percentage_sorted_sales.index, percentage_sorted_sales.values, height=0.7)
plt.title("%Sales by store")
plt.xlabel("%Sales", fontsize = 12)
plt.bar_label(p, fmt = "%.2f")
plt.xlim([0, 20])
plt.show()
