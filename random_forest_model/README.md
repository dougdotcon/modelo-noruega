### README.md

# Olympic Medal Prediction Project

## 1. Project Description

This project aims to develop a predictive model to estimate the number of medals a country may win in the next Olympics. By using historical Olympic performance data, socio-economic indicators such as Gross Domestic Product (GDP), Human Development Index (HDI), and population, the project analyzes how these factors influence a country's Olympic success.

## 2. Project Objectives

- **Main Objective**: Create a machine learning model to predict the number of medals each country may win in the next Olympics.
  
- **Sub-objectives**:
  1. Explore the relationship between socio-economic variables and Olympic performance.
  2. Compare different machine learning algorithms to identify the most effective one.
  3. Provide insights into how socio-economic factors influence Olympic success.

## 3. Project Structure

The project is organized into the following scripts:

- **`data_loading.py`**: Loads data from CSV files into pandas dataframes.
- **`data_preprocessing.py`**: Performs data preprocessing, including handling missing values, normalization, and merging datasets.
- **`model_training.py`**: Trains the Random Forest model with the training data.
- **`model_evaluation.py`**: Evaluates the model's performance using metrics like MAE, MSE, RMSE, and R².
- **`visualizations.py`**: Creates visualizations, such as feature importance plots.
- **`main.py`**: The main script that orchestrates all other scripts and executes the project's complete workflow.