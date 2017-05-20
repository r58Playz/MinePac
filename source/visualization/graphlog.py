import numpy as np
import matplotlib.pyplot as plt

import sys

def rolling_average(l, i, g):
    if i >= len(l):
        i = len(l) - 1

    total = 0
    for k in range(i, max(-1, i - g), -1):
        total += l[k]

    return float(total) / float(g)

def graph_csv(csv, g, cutoff, style):
    X = np.genfromtxt(csv)
    M = len(X)

    if len(X) > cutoff and cutoff > 0:
        X = X[:cutoff]

    avg = np.array([rolling_average(X, i, g) for i in range(M)])

    plt.plot(range(len(avg)), avg, style, lw=3.0)

if __name__ == "__main__": # arg pattern goes [cutoff] [file1] [rolling average 1] [style1] [file2]...
    cutoff = int(sys.argv[1])

    for i in range(2, len(sys.argv), 3):
        graph_csv(sys.argv[i], int(sys.argv[i + 1]), cutoff, sys.argv[i + 2])

    plt.show()
