import numpy as np
import matplotlib.pyplot as plt

import sys
import os.path

def rolling_average(l, i, g):
    if i >= len(l):
        i = len(l) - 1

    total = 0
    for k in range(i, max(-1, i - g), -1):
        total += l[k]

    return float(total) / float(g)

def graph_csv(csv, g, cutoff, logging_level, style):
    X = np.genfromtxt(csv)
    X = np.array([x[-1] for x in X if x[0] <= logging_level])

    M = len(X)

    if len(X) > cutoff and cutoff > 0:
        X = X[:cutoff]

    avg = np.array([rolling_average(X, i, g) for i in range(M)])

    plt.plot(range(len(avg)), avg, style, lw=3.0)

def get_int_param(prompt, default):
    i = None
    while i == None:
        i_str = raw_input(prompt)
        try:
            if i_str == "":
                i = default
            else:
                i = int(i_str)
        except ValueError:
            i = None
            print "ERROR: specified value is not a valid integer"

    return i

def get_file_params(): # returns file name, moving average window size, and logging level
    f = None
    while f == None:
        f = raw_input("Enter the relative path of the log file (or type \"done\" if you are finished specifying files): ")
        if not os.path.isfile(f) and f.lower() != "done":
            f = None
            print "ERROR: specified path is not a file. Please try again."

    if f.lower() == "done":
        return None, None, None

    avg = get_int_param("Enter the moving average window size for these data (or blank if you do not want to average): ", 1)

    logging_level = get_int_param("Enter the logging level (or leave blank to display all entries): ", sys.maxint)

    return f, avg, logging_level

if __name__ == "__main__":
    styles = ['r-', 'g-', 'b-', 'k-', 'm-', 'c-', 'y-']

    cutoff = get_int_param("Enter the number of entries before the graph will cut off (or leave blank for no cutoff): ", 0)

    i = 0
    while True:
        f, avg, llvl = get_file_params()
        if f == None:
            break

        graph_csv(f, avg, cutoff, llvl, styles[i % len(styles)])
        i += 1

    plt.ylabel("score")
    plt.xlabel("mission")
    plt.show()
