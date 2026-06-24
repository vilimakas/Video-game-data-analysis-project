import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video Games Sales (1980-2024) - Raw.csv')

region_totals = df[['na_sales', 'jp_sales', 'pal_sales', 'other_sales']].sum()
print(region_totals)

region_genre = df.groupby("genre")[['na_sales', 'jp_sales', 'pal_sales', 'other_sales']].sum()
print(region_genre)

region_totals.plot(kind='bar')
plt.title("Total Sales by Region")
plt.ylabel("Sales (millions)")
plt.show()
