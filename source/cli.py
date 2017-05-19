import algorithm
import argparse

def algorithmsList():
    l = "available algorithms:\n"

    valid = algorithm.valid_algorithms()
    maxNameLength = 0
    for alg in valid:
        if len(alg) + 2 > maxNameLength: #extra 2 chars for algorithm name + ": "
            maxNameLength = len(alg) + 2

    for alg in valid:
        l += ("    " + (alg + ": ").ljust(maxNameLength) + valid[alg] + "\n")

    return l

def parseArgs():
    parser = argparse.ArgumentParser(
        description = "Agent learns to navigate a maze in Minecraft using local search algorithms",
        epilog = algorithmsList(),
        formatter_class = argparse.RawTextHelpFormatter
    )

    parser.add_argument("maze", help="specifies the maze XML file")
    parser.add_argument("algorithm", help="specifies the name of the algorithm")

    args = parser.parse_args()
    maze, alg = args.maze, algorithm.get(args.algorithm)

    if alg == None:
        print "ERROR: You must specify a valid algorithm."
        print "Use the --help command to see a list of available algorithms."

        exit(1)

    return maze, alg
