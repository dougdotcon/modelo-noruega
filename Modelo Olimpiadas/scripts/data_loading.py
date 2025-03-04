import pandas as pd

def load_data():
    # Carregar os dados de cada arquivo CSV
    gdp_df = pd.read_csv('GDP by Country 1999-2022.csv')
    hdi_df = pd.read_csv('Human Development Index - Full.csv')
    medals_df = pd.read_csv('olympics_medals_country_wise.csv')
    population_df = pd.read_csv('population_by_country_2020.csv')
    
    return gdp_df, hdi_df, medals_df, population_df
