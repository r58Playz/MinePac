from algorithms.genetic import genetic
from algorithms.hillclimbing import climber
from algorithms.annealing import annealing

import heuristics as h

'''
Algorithms must have the following functions defined:
__init__:
	parameters:
		heuristics_list: a list of heuristic functions that the algorithm can use
	returns:
		N/A (constructor)

set_score:
	parameters:
		score: the numerical score of the mission that just completed
	returns:
		nothing

get_action:
	parameters:
		observations: a mission.observation containing the most recent observational data
	returns:
		an action string that can be send to the agent
'''

def get(alg_selected):
	if alg_selected == "genetic":
		return genetic([h.towards_item, h.away_from_enemy, h.random_direction])
	elif alg_selected == "hillclimb" or alg_selected == "hilclimbing":
		return climber([h.towards_item, h.away_from_enemy, h.random_direction])
	elif alg_selected == "annealing" or alg_selected == "anneal":
		return annealing([h.towards_item, h.away_from_enemy, h.random_direction])
	elif alg_selected == "mcts":
		pass
	else: pass

	return None

def valid_algorithms(): # dictionary in format 'algorithm name': 'algorithm description'
	return {
				"genetic": "genetic algorithm operating on strings of movement heuristics",
	 			"hillclimb": "hillclimbing algorithm operating on weighted probabilities of using a heuristic",
				"annealing": "same as the hillclimbing algorithm, but with simulated annealing"
			}
