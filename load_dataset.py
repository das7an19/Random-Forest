import pandas as pd

def load_dataset():

    df = pd.read_csv('your_dataset.csv')


    df_encoded = pd.get_dummies(df, columns=['Shelf Location at stores', 'Education', 'Urban', 'US'])


    X = df_encoded.drop('Target', axis=1)
    y = df_encoded['Target']

    return X, y

