import pandas as pd

df = pd.read_excel("supermarket_sales.xlsx")

df = df[["Gender", "Product line","Total"]]
print(df)
pivot_table = df.pivot_table(index="Gender",columns="Product line", values="Total",aggfunc="sum")
pivot_table.to_csv("pivot_table.csv")