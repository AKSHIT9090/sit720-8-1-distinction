# SIT720 8.1D Distinction Task - Sydney Housing Price Prediction

This project develops a machine learning system to predict Sydney residential property sale prices using a dataset of 100 recently sold properties from Bondi, Campbelltown and Parramatta.

## Project Structure

### dataset
Contains the collected housing dataset in CSV and Excel formats.

### notebook
Contains the Jupyter Notebook with the complete data analysis, feature engineering, model development, evaluation, prediction failure analysis, and ML versus LLM versus human comparison.

### app
Contains the deployed Streamlit web application, trained Gradient Boosting model, and required Python packages.

## Machine Learning Models

Three regression models were developed and evaluated:

- Linear Regression
- Random Forest Regression
- Gradient Boosting Regression

Gradient Boosting with max_depth=4 was selected through the model complexity and validation analysis.

## Web Application

The Streamlit application allows users to enter property characteristics and receive an estimated sale price.

The live deployed application link is provided in the final report.

## Dataset

The dataset contains 100 sold residential properties from:

- Bondi
- Campbelltown
- Parramatta

The dataset includes property characteristics such as bedrooms, bathrooms, parking spaces, listed area, property type, sale date and sale price.

## Limitations

The project uses a relatively small dataset from only three suburbs. Some property characteristics contain missing values, and unusual high-value properties can produce large prediction errors. The model predictions should therefore be treated as estimates rather than exact property valuations.