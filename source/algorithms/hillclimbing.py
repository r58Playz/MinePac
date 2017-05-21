import random

class climber(object):
	def __init__(self, set_actions, init_weights = None):
		self.possible_actions = set_actions
		self.weights = init_weights
		if self.weights == None:
			self.weights = [1] * len(self.possible_actions)

		self.prev_score = 0
		self.h = 0

	def smart_change(self, score): # separate function to support inheritance by the annealing class
		if score > self.prev_score: # if the score is increasing, keep doing what we're doing
			self.weights[self.h] += 1
		else: # if the score is decreasing, maybe we should start preferring other policies
			self.weights[self.h] -= 1
			while True:
				next_action = random.randint(0, len(self.possible_actions) - 1)
				if next_action != self.h:
					self.h = next_action
					break

			self.weights[self.h] += 1

	def set_score(self, score):
		print ("Weights: " + str(self.weights))

		self.smart_change(score)
		self.prev_score = score

	# weighted choice algorithm from http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
	def get_action(self, obs):
		total = sum(self.weights)
		r = random.randint(0, total)
		upto = 0

		for i, w in enumerate(self.weights):
			upto += w
			if upto > r:
				return self.possible_actions[i](obs)

		return self.possible_actions[-1](obs)
