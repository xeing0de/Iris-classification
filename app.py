import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression


def main():
    iris = pd.read_csv("Iris.csv")
    print(iris.head())
    print(iris.info())
    target = "Species"
    X = iris.drop(columns=target)
    y = iris[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=200, random_state=42))
    ])

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}\n")

    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
    print()

if __name__ == "__main__":
    main()

