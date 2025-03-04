import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(gdp_df, hdi_df, medals_df, population_df):
    gdp_df.dropna(inplace=True)
    hdi_df.dropna(inplace=True)
    medals_df.dropna(inplace=True)
    population_df.dropna(inplace=True)

    scaler = MinMaxScaler()
    gdp_df.iloc[:, 1:] = scaler.fit_transform(gdp_df.iloc[:, 1:])
    population_df[['Population']] = scaler.fit_transform(population_df[['Population']])
    hdi_df[['Human Development Index']] = scaler.fit_transform(hdi_df[['Human Development Index']])
    
    merged_df = medals_df.merge(gdp_df, left_on='ioc_code', right_on='Country Code', how='inner')
    merged_df = merged_df.merge(population_df, on='Country', how='inner')
    merged_df = merged_df.merge(hdi_df, on='Country', how='inner')
    
    return merged_df
