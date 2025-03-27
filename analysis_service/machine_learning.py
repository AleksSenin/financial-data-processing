import pandas as pd
from sklearn.linear_model import LinearRegression

def analyze_data(data):
    df = pd.DataFrame(data)
    model = LinearRegression()
    model.fit(df[['feature']], df['price'])
    predictions = model.predict(df[['feature']])
    return predictions

if __name__ == "__main__":
    data = [
        {'feature': 1, 'price': 150.25},
        {'feature': 2, 'price': 151.75},
        {'feature': 3, 'price': 153.00},
    ]
    predictions = analyze_data(data)
    print(predictions)
