# - Write a program to develop the Naive Bayes classifier based on split up of
#  training and testing dataset as 90-10, 70-30.
#   - a) Iris dataset
#   - b) Titanic dataset

# a) Iris data set

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

def naive_bayes_classifier():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

    model = GaussianNB()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Accuracy on Iris Data:", accuracy_score(y_test, predictions))

naive_bayes_classifier()

# b) Titanic dataset

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def naive_bayes_titanic():
    # Load Titanic dataset
    df = sns.load_dataset("titanic")

    # Select useful features and drop rows with missing values
    df = df[["survived", "pclass", "sex", "age", "fare"]].dropna()

    # Encode categorical variable (sex)
    le = LabelEncoder()
    df["sex"] = le.fit_transform(df["sex"])  # male=1, female=0

    # Split features and labels
    X = df[["pclass", "sex", "age", "fare"]]
    y = df["survived"]

    # Split into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train Naive Bayes model
    model = GaussianNB()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Accuracy
    print("Accuracy on Titanic data:", accuracy_score(y_test, predictions))

naive_bayes_titanic()
