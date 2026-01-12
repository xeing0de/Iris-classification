import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")
features = df.drop(columns = ["Species", "Id"])
corr = features.corr()
plt.figure()

plt.imshow(corr, interpolation="nearest")
plt.colorbar(label="Correlation")

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Feature Correlation Matrix")

plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.close()

