import MalmoPython
import os
import sys
import time
import json
import random

import heuristics as h
from mission import mission

m = mission()
m.load(sys.argv[1])

while True:
	m.start()
	#initialize action
	action = ''

	# Loop until mission ends:
	while m.is_running():
		time.sleep(0.1)

		#agent performs movement action here
		observations = m.get_observation()

		########testing observations with a cow and diamond sword
		m.agent_host.sendCommand('chat /summon Item 6 56 0 {Item:{id:minecraft:diamond_sword,Count:1}}')
		m.agent_host.sendCommand('chat /summon Cow 5 56 0')
		#########################################################

		
		'''if action == '' or observations.at_junction():
			action = h.random_direction(observations)
			print
			print action
		m.send_command(action)'''
		m.check_errors()
		
		time.sleep(0.3)

	print
	print ("Mission ended with score " + str(m.block_score()))
	# Mission has ended.
