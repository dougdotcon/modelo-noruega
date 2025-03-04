from scripts.data_loading import load_data
from scripts.data_preprocessing import preprocess_data
from scripts.model_training import train_model
from scripts.model_evaluation import evaluate_model
from scripts.visualizations import plot_feature_importance

def main():
    # Carregar os dados
    gdp_df, hdi_df, medals_df, population_df = load_data()

    # Pré-processar os dados
    merged_df = preprocess_data(gdp_df, hdi_df, medals_df, population_df)

    # Treinar o modelo
    rf_model, X_test, y_test = train_model(merged_df)

    # Avaliar o modelo
    evaluate_model(rf_model, X_test, y_test)

    # Visualizar a importância das variáveis
    plot_feature_importance(rf_model, ['GDP', 'Population', 'Human Development Index'])

if __name__ == "__main__":
    main()
