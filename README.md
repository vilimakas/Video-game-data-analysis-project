# Video Game Sales Analysis

An end-to-end data analytics project exploring global video game sales using **Python** for data analysis and **Tableau** for interactive visualization.

## Project Overview

This project analyzes video game sales data to identify trends across genres, regions, critic scores, and release years. The workflow combines Python for exploratory data analysis (EDA) and Tableau for building an interactive dashboard.

## Tools Used

- Python
- Pandas
- Matplotlib
- Tableau Public

## Dataset

**Source:** https://www.kaggle.com/datasets/bhushandivekar/video-game-sales-and-industry-data-1980-2024

The dataset contains information including:

- Game title
- Genre
- Platform
- Publisher
- Critic score
- Global sales
- Regional sales
- Release date

---

# Tableau Dashboard

Explore the interactive dashboard here:

** Tableau Public**

https://public.tableau.com/views/VideoGameData_17823835098110/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

![Dashboard](video_game_dashboard.png)

# Python Analysis

Python was used to clean the dataset, perform exploratory data analysis, and generate visualizations used to support the Tableau dashboard.

## Total Sales by Genre

Analyzes total global sales for each game genre.

![Genre Sales](python/genre%20sales.png)

---

## Critic Score vs Total Sales

Explores the relationship between critic scores and commercial success.

![Critic Score vs Total Sales](python/critic%20score%20vs%20total%20sales.png)

---

## Regional Sales Breakdown

Compares total sales across different regions.

![Total Sales by Region](python/total%20sales%20by%20region.png)

---

## Genre Sales Over Time

Visualizes how genre popularity changed over the available release years.

![Genre Sales Over Time](python/genre%20sales%20over%20time.png)

---

# Repository Structure

```
.
├── python/
│   ├── genre sales.py
│   ├── genre sales over time.py
│   ├── regional breakdown.py
│   ├── sales vs criticscore.py
│   ├── genre sales.png
│   ├── genre sales over time.png
│   ├── critic score vs total sales.png
│   └── total sales by region.png
│
├── Video Games Sales (1980-2024) - Raw.csv
└── README.md
```

---

# Key Insights

- Action games generated the highest overall sales.
- Regional preferences vary significantly, with Japan showing different genre preferences compared to North America and Europe.
- Critic scores have a weak positive relationship with total sales.
- Genre popularity has evolved considerably over time.
