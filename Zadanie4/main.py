import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data",
                 names = ["animal name", "hair", "feathers", "eggs", "milk", "airborne", "aquatic", "predator", "toothed",
                          "backbone", "breathes", "venomous", "fins", "legs", "tail", "domestic", "catsize", "type"])


def absolute_value(val):
    a  = np.round(val/100.*len(df.index), 0)
    return int(a)


pieCharts = ["feathers", "eggs", "airborne", "predator", "venomous", "tail"]


def create_has_label(characteristic):
    if characteristic == "airborne" or characteristic == "predator" or characteristic == "venomous":
        return ["are " + characteristic, "are not " + characteristic]
    else:
        return ["have " + characteristic, "have no " + characteristic]


for characteristic in pieCharts:
    numberOfAnimalsWithGivenCharacteristic = df[characteristic].sum()
    theRest = len(df.index) - numberOfAnimalsWithGivenCharacteristic

    data = np.array([numberOfAnimalsWithGivenCharacteristic, theRest])
    labels = create_has_label(characteristic)
    plt.pie(data, labels=labels, autopct=absolute_value)
    plt.legend([numberOfAnimalsWithGivenCharacteristic, theRest])
    plt.title("Number of Animals that " + labels[0])
    plt.show()
