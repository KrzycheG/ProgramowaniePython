import pandas
import matplotlib.pyplot as plt
miamiData = pandas.read_csv("Miami 2021-01-01 to 2021-12-31.csv")
warsawData = pandas.read_csv("warsaw 2021-01-01 to 2021-12-31.csv")

dfMiami = miamiData[['temp', 'datetime']]
dfWarsaw = warsawData[['temp', 'datetime']]

dfMiami['datetime'] = pandas.to_datetime(dfMiami['datetime'])
dfWarsaw['datetime'] = pandas.to_datetime(dfWarsaw['datetime'])

miamiGroupedByMonth = dfMiami.groupby(dfMiami.datetime.dt.month).mean().round(2)
warsawGroupedByMonth = dfWarsaw.groupby(dfWarsaw.datetime.dt.month).mean().round(2)

plt.plot(miamiGroupedByMonth.index, miamiGroupedByMonth.temp, label='Miami')
plt.plot(warsawGroupedByMonth.index, warsawGroupedByMonth.temp, label="Warsaw")
plt.xticks(miamiGroupedByMonth.index)
plt.ylabel("Temperature in Celcius")
plt.xlabel("Month")
plt.title("Average temperature by Month 2021")
plt.legend()
plt.savefig('tempCompMiamiWarsaw')
plt.show()
