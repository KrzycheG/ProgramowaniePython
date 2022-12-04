import pandas
import matplotlib.pyplot as plt
import numpy as np

assets = pandas.read_csv("assets.txt", sep='\t')

assets = assets.rename(columns={'Variance ': 'Variance'})
x =  assets.Mean
y =  assets.Variance

a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b

y_err = x.std() * np.sqrt(1/len(x) + (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, axes = plt.subplots()
axes.plot(x, y_est, '-')
axes.fill_between(x, y_est - y_err, y_est + y_err, alpha = 0.2)
axes.plot(x, y, 'o', color='tab:brown')

plt.savefig("result.png", dpi = 200)
plt.show()