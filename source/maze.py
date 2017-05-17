import MalmoPython
import os
import sys
import time
import json
import random

from mission import mission

import algorithm
import heuristics as h

m = mission()
m.load(sys.argv[1])

g = algorithm.get([h.away_from_enemy, h.towards_item, h.random_direction])

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
		m.stop_clock()
		m.check_errors()
		
	m.stop_clock()
	
	print
	print ("Mission ended with score: " + str(m.score()))
	g.set_score(m.score())
	
	m.send_command("chat /clear")
	m.send_command("chat /kill @e[type=Player]")
	
	# Mission has ended.
