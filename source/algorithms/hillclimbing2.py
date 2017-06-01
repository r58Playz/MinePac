###################
#same as hillclimbing but explores fewer neighbors
#runs through each iteration more quickly
###################

import random

from algorithm import algorithm

class climber2(algorithm):
	def __init__(self, set_actions, init_eps = 0.0, set_cooling = 1.0, init_str = []):
		super(climber2, self).__init__(set_actions)

		self.h_str = []
		self.possible_actions = set_actions

		self.local_space = self.generate_local_space()

		self.neighbor_scores = []
		self.move = 0
		self.space_index = 0
		self.current_score = 0

		self.eps = init_eps
		self.cooling_rate = set_cooling

	def generate_local_space(self):
                if len(self.h_str) == 0:
                        self.h_str = [random.choice(self.possible_actions)]
                        return [self.h_str]

		space = [self.h_str]

		for i in range(0, len(self.h_str)): # add all remove changes
			r = list(self.h_str)
			del r[i]
			if len(r) > 0:
				space.append(r)

		for i in range(0, len(self.h_str)): # add all mutate changes
			for h in self.possible_actions:
				if self.h_str[i] != h:
					m = list(self.h_str)
					m[i] = h
					space.append(m)

		for i in range(0, len(self.h_str) + 1): # add all insertion changes
			for h in self.possible_actions:
				a = list(self.h_str)
				a.insert(i, h)
				space.append(a)

		space = [list(x) for x in set(tuple(x) for x in space)] #make sure all neighbors are unique

		random.shuffle(space)

		return space

	def pick_best_neighbor(self):
		self.space_index = 0

                best_score = 0
                best_neighbor = None # find the neighbor with the best score, then start looking from there

                for i, s in enumerate(self.neighbor_scores):
                        if s > best_score:
                                best_score = s
                                best_neighbor = self.local_space[i]

		self.h_str = best_neighbor
		self.current_score = best_score
		self.neighbor_scores = []

		self.local_space = self.generate_local_space()


	def process_score(self, score):
                r = random.random()

		self.neighbor_scores.append(score)
		self.move = 0
		log_score = 1

                # if we have searched all neighbors, found an improvement, or if annealing occurs
		if self.current_score < score or r < self.eps:
                        #############update epsilon here
                        log_score = 0
                        self.h_str = self.local_space[self.space_index]
			self.current_score = score
			print ("String updated. New string: " + str([h.__name__[0] for h in self.h_str]))
			print
			self.local_space = self.generate_local_space()
			self.space_index = 0
			self.neighbor_scores = []
		elif self.space_index >= len(self.local_space):
                        #when local maxima is reached, continue by picking best neighbor
                        print("Reached local maxima: " + str(self.current_score))
                        print("Current string: " + str([h.__name__[0] for h in self.h_str]))
                        self.pick_best_neighbor()
                        print("Picking best neighbor: " + str([h.__name__[0] for h in self.h_str]))
                        print("New score: " + str(self.current_score))
		else:
                        self.space_index += 1

		return [(log_score, score)]

	def get_action(self, obs):
                if self.move == 0:
                        print
                        print ("String: " + str([h.__name__[0] for h in self.local_space[self.space_index]]))

		curr_str = self.local_space[self.space_index]
		a = curr_str[self.move % len(curr_str)]

		self.move += 1
		return a(obs)
