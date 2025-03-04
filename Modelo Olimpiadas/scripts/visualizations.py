import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names):
    # Importância das variáveis no modelo
    importance = model.feature_importances_
    plt.bar(feature_names, importance)
    plt.xlabel('Variável')
    plt.ylabel('Importância')
    plt.title('Importância das Variáveis no Modelo Random Forest')
    plt.show()
