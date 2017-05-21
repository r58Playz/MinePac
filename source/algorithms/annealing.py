import random
from hillclimbing import climber

class annealing(climber):
    def __init__(self, set_actions, init_weights = None, set_cooling = .97):
        super(annealing, self).__init__(set_actions, init_weights)

        self.cooling_rate = set_cooling
        self.eps = 1.0

    def random_change(self, score):
        self.h = random.randint(0, len(self.possible_actions) - 1)
        self.weights[self.h] += 1

    def set_score(self, score):
        print ("Weights: " + str(self.weights) + ", Epsilon = " + str(self.eps))
        r = random.random()
        if r < self.eps:
            self.random_change(score)
        else:
            self.smart_change(score)

        self.eps *= self.cooling_rate
        self.prev_score = score
