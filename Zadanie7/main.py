import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# breaking down fuctions to avoid duplicated code - DRY
def shubert_partial(val):
    return (np.cos(2 * val + 1)) + (2 * np.cos(3 * val + 2)) + (3 * np.cos(4 * val + 3)) + (4 * np.cos(5 * val + 4)) + (5 * np.cos(6 * val + 5))


def rastring_partial(val):
    return pow(val, 2) - np.cos(18 * np.pi * val)


# functions
def alpian2(x, y):
    return np.cos(x) * x *(1+(np.cos(y)/2))


def shubert(x, y):
    return shubert_partial(x) * shubert_partial(y)


def rastrigin(x, y):
    return rastring_partial(x) + rastring_partial(y)


# method which create fig and save it to file
def create_save(X, Y, Z, function_name):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, cmap='magma')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.savefig(function_name, dpi=200)


listOfFunctions = [alpian2, shubert, rastrigin]

for function in listOfFunctions:
    x = np.linspace(-400, 400, 200)
    y = np.linspace(-400, 400, 200)

    X, Y = np.meshgrid(x, y)
    Z = function(X, Y)
    create_save(X, Y, Z, function.__name__)






