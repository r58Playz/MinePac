from genetic import genetic
from hillclimbing import climber

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

def get(alg_selected, heuristics_list):
	if alg_selected == "genetic":
		return genetic(heuristics_list)
	elif alg_selected == "hillclimb":
		return climber(heuristics_list)
	elif alg_selected == "mcts":
		pass
	else: pass
		
