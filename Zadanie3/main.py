import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                 names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"])
colors = {"Iris-setosa": "red", "Iris-versicolor": "blue", "Iris-virginica": "green"}
print(df)

plt.scatter(df["Sepal Length"], df["Sepal Width"], c=df["Class"].map(colors))
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()
plt.scatter(df["Petal Length"], df["Petal Width"], c=df["Class"].map(colors))
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()
plt.scatter(df["Sepal Length"], df["Petal Width"], c=df["Class"].map(colors))
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.show()
plt.scatter(df["Petal Length"], df["Sepal Width"], c=df["Class"].map(colors))
plt.xlabel("Petal Length")
plt.ylabel("Sepal Width")
plt.show()

