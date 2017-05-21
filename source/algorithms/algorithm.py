import abc

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

class algorithm(object):
	def __init__(self, set_actions):
		self.possible_actions = set_actions

	@abc.abstractmethod
	def set_score(self, score):
		raise NotImplementedError

	@abc.abstractmethod
	def get_action(self, obs):
		raise NotImplementedError
