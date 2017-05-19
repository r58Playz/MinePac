import random

class genetic:
	def __init__(self, set_actions, set_gen_size = 20, set_str_len = 5, set_sel_frac = .25):
		self.possible_actions = set_actions
		self.generation_size = set_gen_size
		self.str_len = set_str_len
		self.selection_fraction = int(set_sel_frac * self.generation_size)

		self.iteration = 0
		self.move = 0

		self.scores = [0] * self.generation_size

		self.population = []
		for i in range(self.generation_size):
			l = int(random.gauss(self.str_len, self.str_len / 2)) # strings of random gaussian length
			if l < 1:
				l = 1

			actions = []
			for j in range(0, l):
				actions.append(random.choice(self.possible_actions))

			self.population.append(actions)

	def set_score(self, score):
		self.scores[self.iteration % self.generation_size] = score
		if self.iteration != 0 and self.iteration % self.generation_size == 0:
			self.next_generation()

		self.iteration += 1
		self.move = 0

		print ("Next action string: " + str([f.__name__[0] for f in self.population[self.iteration % self.generation_size]]))

	def get_action(self, obs):
		policy = self.population[self.iteration % self.generation_size]
		action = policy[self.move % len(policy)](obs)

		self.move += 1
		return action

	def next_generation(self):
		print ("Creating next generation...")
		new_population = []
		best_scores = []
		fittest = []

		#find the best scores in the population
		for i, s in enumerate(reversed(sorted(self.scores))):
			if i > self.selection_fraction:
				break
			best_scores.append(s)

		#now select every string in the population that has one of the best scores
		for i, p in enumerate(self.population):
			if self.scores[i] in best_scores:
				fittest.append(p)

		#now generate the next generation of heuristic function strings
		for i in range(self.generation_size):
			first_parent = random.choice(fittest)
			second_parent = random.choice(fittest)

			crossover = random.random()
			first_crossover = int(crossover * (len(first_parent) - 1))
			second_crossover = int(crossover * (len(second_parent) - 1))

			child = first_parent[:first_crossover] + second_parent[second_crossover:]
			new_population.append(child)

		self.population = new_population
		self.scores = [0] * self.generation_size
