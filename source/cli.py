import algorithm
import argparse

import time
import os

def algorithmsList():
    l = "available algorithms:\n"

    valid = algorithm.valid_algorithms()
    maxNameLength = 0
    for alg in valid:
        if len(alg) + 3 > maxNameLength: #extra 3 spaces of padding
            maxNameLength = len(alg) + 3

    for alg in valid:
        l += ("  " + alg.ljust(maxNameLength) + valid[alg] + "\n")

    return l

def parseArgs():
    parser = argparse.ArgumentParser(
        description = "Agent learns to navigate a maze in Minecraft using local search algorithms",
        epilog = algorithmsList(),
        formatter_class = argparse.RawTextHelpFormatter
    )

    parser.add_argument("maze", help="specifies the maze XML file")
    parser.add_argument("algorithm", help="specifies the name of the algorithm")
    # parser.add_argument("-f", "--file", type=str, help="specifies the name of the output log file (named with the timestamp by default)") # optional arguments not working for some reason

    args = parser.parse_args()
    maze = args.maze
    alg = algorithm.get(args.algorithm)
    #if not args.file:
    out_file = "logs/log_" + args.algorithm + "_" + str(time.time()) + ".csv"
    if not os.path.exists("logs"):
        os.makedirs("logs")
    #else:
    #    out_file = args.file

    if alg == None:
        print "ERROR: You must specify a valid algorithm."
        print "Use the --help command to see a list of available algorithms."

        exit(1)

    return maze, alg, out_file
