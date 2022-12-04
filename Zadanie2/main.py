import pandas
import matplotlib.pyplot as plt
assets = pandas.read_csv("assets.txt", sep='\t')
paretoFront = pandas.read_table("Pareto Front.txt", sep='\t')
assets = assets.rename(columns={'Variance ': 'Variance'})
paretoFront = paretoFront.rename(columns={'Mean ': 'Mean'})
print(paretoFront.columns)

plt.scatter(paretoFront.Variance, paretoFront.Mean)
plt.colorbar()
plt.xlabel("Variance")
plt.ylabel("Mean")
plt.scatter(assets.Variance, assets.Mean, c =assets.Variance, cmap='Spectral')

plt.show()
print(assets.Variance)
