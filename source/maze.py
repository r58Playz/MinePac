import MalmoPython
import os
import sys
import time
import json
import random

from genetic import genetic
from hillclimbing import climber
from mission import mission

import heuristics as h

m = mission()
m.load(sys.argv[1])

g = genetic([h.away_from_enemy, h.towards_item, h.random_direction])

while True:		
	m.start()
	#initialize action
	action = ''

	# Loop until mission ends:
	try:
		while m.is_running():
			time.sleep(0.1)

			#agent performs movement action here
			observations = m.get_observation()
			if action == '' or observations.at_junction():
				action = g.get_action(observations)
				#print action
				
			m.send_command(action)
			m.check_errors()
		
			time.sleep(0.1)
	except Exception as e:
		print ("ERROR: " + str(e))
		
		m.send_command("quit")
		m.check_errors()
		

	print
	print ("Mission ended with score: " + str(m.item_score()))
	g.set_score(m.item_score())
	
	m.send_command("chat /clear")
	m.send_command("chat /kill @e[type=Player]")
	
	# Mission has ended.
