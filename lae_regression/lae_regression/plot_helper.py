"""
Helper to plot one dimensional regression fits using matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

def lsqfit(x, y):
    "least squares fit, for comparison"
    x = np.array(x)
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y)[0]
    fity = m*x + c
    return fity

def plot(result, size=64):
    samples = result["samples"]
    dimensions = result["dimensions"]
    # this plot only works for linear fits
    assert dimensions == 1, "sorry, no can do"
    U = result["U"]
    m = result["m"]
    x = U.reshape((samples,))
    y_actual = result["v"]
    y_predicted = result["v_predicted"]
    y_least_squares = lsqfit(x, y_actual)
    fig, ax = plt.subplots()
    ax.scatter(x, y_actual, facecolors='none', edgecolors='b', s=size)
    #ax.scatter(x, y_predicted, color="red", marker="x", s=size)
    ax.plot(x, y_least_squares, color="green", dashes=(5,5))
    ax.plot(x, y_predicted, color="red")
    fig.show()
