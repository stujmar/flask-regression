def apply_regression(data):
    """
    Apply regression to data
    """
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.pipeline import make_pipeline
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings("ignore")

    # Create pipeline
    pipeline = make_pipeline(PolynomialFeatures(2), LinearRegression())

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data.iloc[:, -1], test_size=0.2, random_state=42)

    # Fit pipeline
    pipeline.fit(X_train, y_train)

    # Predict
    y_pred = pipeline.predict(X_test)

    # Calculate error
    error = mean_squared_error(y_test, y_pred)

    # Print error
    print("Error:", error)

    # Plot
    plt.scatter(y_test, y_pred)
    plt.xlabel("True Values")
    plt.ylabel("Predictions")
    plt.show()

    # Return pipeline
    return pipeline

def simple_results(data):
    """
    Pass in json of key data pairs and return a density plot of the data.
    """
    pass