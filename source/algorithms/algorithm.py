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
		a list of tuples [(logging_level, score)]
		score:
			the score that will be logged
		logging_level:
		 	used to filter out scores when processing data
			the higher the logging level, the less important the score

get_action:
	parameters:
		observations: a mission.observation containing the most recent observational data
	returns:
		an action string that can be send to the agent
'''

class algorithm(object):
	log_file = "" # static field, set in cli

	def __init__(self, set_actions):
		self.possible_actions = set_actions

	@abc.abstractmethod
	def process_score(self, score):
		raise NotImplementedError

	@abc.abstractmethod
	def set_score(self, score):
		log_lines = self.process_score(score)
		
		with open(algorithm.log_file, "a+") as log:
			for logging_level, s in log_lines:
				log.write(str(logging_level) + "," + str(s) + "\n")

	@abc.abstractmethod
	def get_action(self, obs):
		raise NotImplementedError
