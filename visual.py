import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def save_decision_zones(model, df, features, target_col, out_path):
    x_col, y_col = features

    X = df[[x_col, y_col]]
    y = df[target_col]

    x_min, x_max = X[x_col].min() - 0.3, X[x_col].max() + 0.3
    y_min, y_max = X[y_col].min() - 0.3, X[y_col].max() + 0.3

    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.02),
        np.arange(y_min, y_max, 0.02),
    )

    grid = pd.DataFrame(
        np.c_[xx.ravel(), yy.ravel()],
        columns=[x_col, y_col]
    )

    pred = model.predict(grid).reshape(xx.shape)

    classes = np.unique(y)
    class_to_int = {cls: i for i, cls in enumerate(classes)}
    pred_int = np.vectorize(class_to_int.get)(pred)

    plt.figure()

    plt.contourf(xx, yy, pred_int, alpha=0.25)

    for cls in classes:
        subset = df[df[target_col] == cls]
        plt.scatter(
            subset[x_col],
            subset[y_col],
            s=20,
            alpha=0.85,
            label=cls,
        )

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.title(f"{x_col} + {y_col}")
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()

