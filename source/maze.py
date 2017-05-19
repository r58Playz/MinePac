import MalmoPython
import time

import cli
from mission import mission

if __name__ == "__main__":
	mazeXMLFile, a = cli.parseArgs()

	m = mission()
	m.load(mazeXMLFile)

	## need a method to incorporate all the algorithms (i.e. for alg in alg_list: try)

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
					action = a.get_action(observations)
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

		print ("\nMission ended with score: " + str(m.score()))
		a.set_score(m.score())

		m.send_command("chat /clear")
		m.send_command("chat /kill @e[type=Player]")

	# Mission has ended.
