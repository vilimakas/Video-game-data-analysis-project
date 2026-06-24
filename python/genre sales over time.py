import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video Games Sales (1980-2024) - Raw.csv')

df_time = df[df['release_date'].notna()].copy()

df_time['release_date'] = pd.to_datetime(df_time['release_date'], dayfirst=True, errors='coerce')
df_time['year'] = df_time['release_date'].dt.year

genre_year = df_time.groupby(['year', 'genre'], as_index=False)['total_sales'].sum()

top_genres = (
    df_time.groupby('genre')['total_sales']
    .sum()
    .nlargest(5)
    .index
)

filtered = genre_year[genre_year['genre'].isin(top_genres)]

plt.figure(figsize=(12,6))

for genre in top_genres:
    data = filtered[filtered['genre'] == genre].sort_values('year')
    plt.plot(data['year'], data['total_sales'], label=genre)

plt.title("Genre Sales Over Time (Top 5 Genres)")
plt.xlabel("Year")
plt.ylabel("Total Sales (Millions)")
plt.legend()
plt.grid(True)
plt.show()