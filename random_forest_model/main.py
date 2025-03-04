from scripts.data_loading import load_data
from scripts.data_preprocessing import preprocess_data
from scripts.model_training import train_model
from scripts.model_evaluation import evaluate_model
from scripts.visualizations import plot_feature_importance

def main():
    gdp_df, hdi_df, medals_df, population_df = load_data()

    merged_df = preprocess_data(gdp_df, hdi_df, medals_df, population_df)

    rf_model, X_test, y_test = train_model(merged_df)

    evaluate_model(rf_model, X_test, y_test)

    plot_feature_importance(rf_model, ['GDP', 'Population', 'Human Development Index'])

if __name__ == "__main__":
    main()
