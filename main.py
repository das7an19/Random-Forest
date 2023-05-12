import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('your_dataset.csv')

df_encoded = pd.get_dummies(df, columns=['Shelf Location at stores', 'Education', 'Urban', 'US'])

X = df_encoded.drop('Target', axis=1)
y = df_encoded['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier()
rf_classifier.fit(X_train, y_train)

accuracy = rf_classifier.score(X_test, y_test)
print("Accuracy:", accuracy)
