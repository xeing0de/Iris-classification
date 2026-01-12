import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression


def main():
    iris = pd.read_csv("Iris.csv")
    print(iris.head(), end = "\n\n")
    iris.info()
    print()

    target = "Species"
    features = ["SepalLengthCm",
                "SepalWidthCm",
                "PetalLengthCm",
                "PetalWidthCm",
                ]
    allmodel = Model(iris, features, target)

    models = []
    for i in range(len(features)):
        for j in range(i+1, len(features)):
            feat_pair = [features[i], features[j]]
            models.append(Model(iris, feat_pair, target))
    
    allmodel.fit()
    for i in models:
        i.fit()

    y_all = allmodel.predict()
    acc = accuracy_score(allmodel.y_test, y_all)
    print(f"Accuracy for all features: {acc:.4f}")

    print("Confusion matrix:")
    print(confusion_matrix(allmodel.y_test, y_all), end = "\n\n")

    for i in models:
        y_pred = i.predict()
        acc = accuracy_score(i.y_test, y_pred)
        print(f"Accuracy for {i.features}: {acc:.4f}")
        
        print("Confusion matrix:")
        print(confusion_matrix(i.y_test, y_pred), end = "\n\n")



class Model():
    def __init__(self, dataset, features, target):
        self.features = " + ".join(features)
        self.X = dataset[features]
        self.Y = dataset[target]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.X,
                self.Y,
                test_size=0.2,
                random_state=42,
                stratify=self.Y,
                )
        
        self.model = Pipeline(steps=[
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=200, random_state=42)),
        ])

    def fit(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self):
        return self.model.predict(self.X_test)
        

if __name__ == "__main__":
    main()

