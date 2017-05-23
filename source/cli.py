import argparse
import time
import os

from algorithms.genetic import genetic
from algorithms.hillclimbing import climber
from algorithms.hillclimbing2 import climber2
from algorithms.brute import brute

import heuristics as h

def get_algorithm(alg_selected):
    if alg_selected == "genetic":
        return genetic([h.towards_item, h.away_from_enemy, h.random_direction])
    elif alg_selected == "hillclimb" or alg_selected == "hillclimbing":
        return climber([h.towards_item, h.away_from_enemy])#, h.random_direction])
    elif alg_selected == "annealing" or alg_selected == "anneal":
        return climber([h.towards_item, h.away_from_enemy], 1.0, 0.5)#, h.random_direction])
    elif alg_selected == "hillclimb2" or alg_selected == "hillclimbing2":
        return climber2([h.towards_item, h.away_from_enemy])
    elif alg_selected == "annealing2" or alg_selected == "anneal2":
        return climber2([h.towards_item, h.away_from_enemy], 1.0, 0.5)
    elif alg_selected == "brute":
        return brute([h.towards_item, h.away_from_enemy, h.random_direction])
    elif alg_selected == "mcts":
        pass
    else: pass

    return None

def valid_algorithms(): # dictionary in format 'algorithm name': 'algorithm description'
    return {
                "genetic": "genetic algorithm operating on strings of movement heuristics",
                "hillclimb": "hillclimbing algorithm operating on strings of movement heuristics",
                "annealing": "same as the hillclimbing algorithm, but with simulated annealing",
                "hillclimb2": "hillclimbing that explores fewer neighboring states. Each iteration should be much quicker",
                "annealing2": "simulated annealing using the hillclimb2 modifications",
                "brute": "brute force method of finding optimal solution by exploring all possible string combinations"
            }

def algorithms_list():
    l = "available algorithms:\n"

    valid = valid_algorithms()
    maxNameLength = 0
    for alg in valid:
        if len(alg) + 3 > maxNameLength: #extra 3 spaces of padding
            maxNameLength = len(alg) + 3

    for alg in valid:
        l += ("  " + alg.ljust(maxNameLength) + valid[alg] + "\n")

    return l

def parse_args():
    parser = argparse.ArgumentParser(
        description = "Agent learns to navigate a maze in Minecraft using local search algorithms",
        epilog = algorithms_list(),
        formatter_class = argparse.RawTextHelpFormatter
    )

    parser.add_argument("maze", help="specifies the maze XML file")
    parser.add_argument("algorithm", help="specifies the name of the algorithm")
    # parser.add_argument("-f", "--file", type=str, help="specifies the name of the output log file (named with the timestamp by default)") # optional arguments not working for some reason

    args = parser.parse_args()
    maze = args.maze
    alg = get_algorithm(args.algorithm)
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
