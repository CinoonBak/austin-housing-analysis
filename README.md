# Austin-Housing-Analysis
Collection of visualizations, clustering analysis, gradient boosting classifier, and a local website to view current listing of houses on sale in Austin, TX. 
# Project Overview
* Using Zillow, collected all houses on sale in Austin, TX.
* Zillow has strong protection/lazy loading, therefore I used bardeen to scarpe the data on the website. 
* Cleaned and processed data to be used for eda and machine learning. 
* Used visualzation tools to analyze Austin houses. 
* Optimized clustering analysis to learn which areas in Austin are similar to each other in terms of houses. 
* Made a website optimizing gradient boosing classifier to classify the zip code for the users need in bed number, bath number, price, and square feet. 
# Code & Resources Used
Python Version: 3.9.12 | Tableau Public | Sublime Text
* Python Packages: pandas, numpy, sklearn, matplotlib, seaborn, kmeans, flask, gradinetboostingclassifier
* Finding Optimal Cluster Number: https://towardsdatascience.com/cheat-sheet-to-implementing-7-methods-for-selecting-optimal-number-of-clusters-in-python-898241e1d6ad
# Data Collection
* Using Bradeen, scraped about 1,000 houses on sale in the Austin, TX area. 
* Beautiful Soup doesn't work currently to scrape data on Zillow because of their lazy loading on the website. 
* Collected only houses excluding apartments, condos, and townhouses.
# Data Cleaning
After collecting the data I have made the following changes: 
* Made a column of just the street names
* Made a column of zipcodes
* Dropped all null values
* Deleted all duplicated houses
* Renamed column names
# EDA
I have visualized through Tableau Public and Matplotlib. Here are some of the foundings: 
* Even though some houses skewed the data, the mean price for houses in this data set is about a million dollars. 
* Mean bed number is 3 and mean bath number is 2. 
* Mid West of Austin has the biggest and the most expensive houses. 
* Price and square fit have a strong correlation to each other. 

![AVGPrice](https://user-images.githubusercontent.com/118776460/231271052-9194a720-0499-4f17-b164-f453dccfcefd.png)
<img width="395" alt="Screen Shot 2023-04-11 at 2 40 39 PM" src="https://user-images.githubusercontent.com/118776460/231271125-9e529fd4-f17f-4f38-b0a7-c21b3898b125.png">
<img width="422" alt="Screen Shot 2023-04-11 at 2 41 06 PM" src="https://user-images.githubusercontent.com/118776460/231271214-f54f9a1f-84fa-4d47-8918-2505dad0b060.png">

# Data Preprocessing
* I have only included bed, bath, sqft, and price as the cluster columns
* I have scaled all of my columns to standardize the numeric values
# Optimal Cluster Numbers
I have used Elbow method, Siluhouette Score method, Calinski Harabasz method, Dendrogram to find the optimal cluster numbers. Below were the outcomes
* Elbow method: 9
* Siluhouette Score: 2
* Calinski Harabasz method: 3
* Dendrogram: 4
# Model Building
* Even though most of the methods suggested me to use lower number of clusers, however, I chose to use 10 clusters since I wanted more specific classifier and all of the methods second best optimal cluster number was close to 10. 
* 
