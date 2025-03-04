import matplotlib.pyplot as plt

def plot_feature_importance(model, feature_names):
    importance = model.feature_importances_
    plt.bar(feature_names, importance)
    plt.xlabel('Variable')
    plt.ylabel('Importance')
    plt.title('Variable Importance in the Random Forest Model')
    plt.show()
