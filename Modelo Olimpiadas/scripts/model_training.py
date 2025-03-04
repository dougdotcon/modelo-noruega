from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(merged_df):
    # Separar variáveis independentes e dependentes
    X = merged_df[['GDP', 'Population', 'Human Development Index']]
    y = merged_df['total_total']

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, max_depth=10, min_samples_split=2, min_samples_leaf=1)
    rf_model.fit(X_train, y_train)
    
    return rf_model, X_test, y_test
