# 🚀 SpaceX Falcon 9 Landing Prediction — Data Science Capstone

## Overview

This project applies the full data science lifecycle — data collection, wrangling, exploratory analysis, interactive visualization, and machine learning — to a real-world problem: **predicting whether the first stage of a SpaceX Falcon 9 rocket will land successfully.**

SpaceX advertises Falcon 9 launches at $62 million, largely because they recover and reuse the first stage. A competing launch provider could estimate launch costs more accurately by predicting landing success ahead of time. This project builds that predictive model from scratch.

## Business Problem

If we can determine whether the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against SpaceX for a rocket launch, informing pricing strategy and competitive analysis.

## Project Structure

├── Notebooks/ # Jupyter notebooks for each stage of the pipeline
│ ├── lab1_data_collection_api.ipynb
│ ├── lab2_web_scraping.ipynb
│ ├── lab3_data_wrangling.ipynb
│ ├── lab4_eda_visualization.ipynb
│ ├── lab5_eda_sql.ipynb
│ ├── lab6_folium_map.ipynb
│ ├── lab8_predictive_analysis.ipynb
│ └── spacex_capstone_master.ipynb # Full end-to-end run with saved outputs
│
├── Data/ # Datasets produced at each pipeline stage
│ ├── dataset_part_1.csv # Cleaned SpaceX API data
│ ├── spacex_web_scraped.csv # Wikipedia-scraped launch records
│ ├── dataset_part_2.csv # Wrangled data with landing outcome labels
│ └── dataset_part_3.csv # One-hot encoded feature matrix (ML-ready)
│
├── Maps/ # Interactive Folium visualizations
│ ├── launch_sites_map.html
│ ├── launch_outcomes_map.html
│ └── proximity_analysis_map.html
│
└── dashboard/ # Interactive Plotly Dash app
└── spacex_dash_app.py


## Methodology

1. **Data Collection**
   - Pulled historical launch records from the public [SpaceX REST API](https://api.spacexdata.com)
   - Scraped a supplementary launch history table from Wikipedia using BeautifulSoup

2. **Data Wrangling**
   - Cleaned and merged datasets
   - Engineered a binary `Class` label (1 = successful landing, 0 = failure) from the raw landing outcome field

3. **Exploratory Data Analysis**
   - Visual EDA with Matplotlib/Seaborn: payload mass, launch site, and orbit vs. landing outcome; yearly success trends
   - SQL-based EDA (SQLite): launch site summaries, payload statistics, success rate rankings, time-based queries

4. **Interactive Visual Analytics**
   - **Folium** map of all launch sites, color-coded launch outcomes, and proximity analysis (distance to nearest coastline)
   - **Plotly Dash** dashboard with a launch-site selector, success/failure pie chart, and payload-vs-outcome scatter plot with a payload range slider

5. **Predictive Analysis**
   - Trained and tuned four classifiers with `GridSearchCV`: Logistic Regression, Support Vector Machine, Decision Tree, and K-Nearest Neighbors
   - Evaluated each with accuracy and confusion matrices on a held-out test set
   - Compared models and selected the best-performing one

## Key Findings

*(Fill in with your actual numbers once you've reviewed your notebook outputs)*
- Overall landing success rate: **__%**
- Best-performing model: **__** with test accuracy of **__%**
- Launch success strongly correlated with: **__** (e.g. orbit type, flight number, payload mass)

## Tools & Technologies

`Python` · `Pandas` · `NumPy` · `Requests` · `BeautifulSoup4` · `Matplotlib` · `Seaborn` · `SQLite` · `Folium` · `Plotly Dash` · `Scikit-learn`

## How to Run

1. Clone this repository
2. Install dependencies: `pip install pandas numpy requests beautifulsoup4 matplotlib seaborn folium dash plotly scikit-learn`
3. Open any notebook in `Notebooks/` with Jupyter or Google Colab and run all cells
4. To launch the interactive dashboard: `cd dashboard && python spacex_dash_app.py`, then open `http://127.0.0.1:8050` in your browser

## Author

Muhammad Talha — built as the final capstone project for the IBM Applied Data Science Capstone / Data Science Professional Certificate.
## Author

*(Your name)* — built as the final capstone project for the IBM Applied Data Science Capstone / Data Science Professional Certificate.
