import pandas as pd

df = pd.read_csv('Video Games Sales (1980-2024) - Raw.csv')


df_sales = df[df['total_sales'].notna()]
genre_sales = df_sales.groupby("genre")['total_sales'].sum().sort_values(ascending=False)
genre_count = df_sales.groupby("genre")["title"].count().sort_values(ascending=False)
genre_avg = genre_sales / genre_count
print(genre_sales, genre_count, genre_avg.sort_values(ascending=False))
