import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


df = pd.read_csv('Video Games Sales (1980-2024) - Raw.csv')

df_score = df[df['critic_score'].notna() & df['total_sales'].notna()]
df_corr = df_score[['critic_score', 'total_sales']].corr()

r, p = pearsonr(df_score['critic_score'], df_score['total_sales'])

print("Correlation:", round(r, 3))
print("P-value:", round(p, 3))

print(df_corr)

plt.scatter(df_score['critic_score'], df_score['total_sales'], alpha=0.3)
plt.xlabel("Critic Score")
plt.ylabel("Total Sales")
plt.title("Critic Score vs Sales")
plt.show()