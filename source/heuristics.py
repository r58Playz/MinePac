import random

def random_direction(obs):
	actions_list = []
	if(obs.grid[1] == u'glowstone'):
		actions_list.append('movenorth 1')
	if(obs.grid[3] == u'glowstone'):
		actions_list.append('movewest 1')
	if(obs.grid[5] == u'glowstone'):
		actions_list.append('moveeast 1')
	if(obs.grid[7] == u'glowstone'):
		actions_list.append('movesouth 1')

	r = random.random()
	a = random.randint(0, len(actions_list) - 1)
	return actions_list[a]
    
def away_from_edges(obs):
	min_dist = min(obs.edge_distances)

	actions_list = []
	if obs.edge_distances[0] == min_dist and obs.grid[7] == u'glowstone':
		actions_list.append('movesouth 1')
	if obs.edge_distances[1] == min_dist and obs.grid[3] == u'glowstone':
		actions_list.append('movewest 1')
	if obs.edge_distances[2] == min_dist and obs.grid[1] == u'glowstone':
		actions_list.append('movenorth 1')
	if obs.edge_distances[3] == min_dist and obs.grid[5] == u'glowstone':
		actions_list.append('moveeast 1')
	
	if len(actions_list) == 0:
		return random_direction(obs)
	
	a = random.randint(0, len(actions_list) - 1)
	return actions_list[a]