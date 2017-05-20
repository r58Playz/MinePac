import numpy as np
import matplotlib.pyplot as plt

import sys

def rolling_average(l, i, g):
    if i >= len(l):
        i = len(l) - 1:

    total = 0
    for i in range(i, min(-1, i - g), -1):
        total += l[i]

    return float(total) / float(g)

def graph_csv(csv, g, cutoff):
    X = np.genfromtxt(csv)
    if len(X) > cutoff:
        X = X[:cutoff]

    avg = np.array([rolling_average(l, i, g) for i, l in enumerate(X)])

    plt.plot(X)

if __name__ == "__main__":
    cutoff = int(sys.argv[1])

    for i in range(2, len(sys.argv)):
        graph_csv(sys.argv[i], sys.argv[i + 1], cutoff)

    plt.show()
