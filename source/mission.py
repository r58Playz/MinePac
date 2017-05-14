import MalmoPython
import os
import sys
import time
import json
import random
import math

class observation:
        def __init__(self, set_grid, set_edge_distances, set_cell):
                self.grid = set_grid
                self.edge_distances = set_edge_distances
                self.agent_cell = set_cell
                
        def at_junction(self):
                '''
                checks if agent is at a junction given the floor grid
                '''               
                neighbor_indices = [1,3,5,7]
                possible_paths = []
                for i in neighbor_indices:
                        if self.grid[i] == u'glowstone':
                                possible_paths.append(self.grid[i])
                if len(possible_paths) == 1:
                        return True
                
                if(self.grid[1] == u'glowstone' or self.grid[7] == u'glowstone'):
                        return self.grid[3] == u'glowstone' or self.grid[5] == u'glowstone'
                if(self.grid[3] == u'glowstone' or self.grid[5] == u'glowstone'):
                        return self.grid[1] == u'glowstone' or self.grid[7] == u'glowstone'

                #this will probably never get called
                #return true just to allow policy evaluation if it does get called
                #may change this later
                return True
        

class mission:
        def __init__(self):
                self.missionXML = ""
                self.agent_host = None
                self.malmo_mission = None
                self.malmo_mission_record = None
                self.world_state = None
                
                self.agent_location = (None, None)
                self.blocks_traveled = {} # dictionary mapping an (x,z) coordinate to the number of times the agent has been there

        def load(self, mission_file):
                sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

                # More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"
                # flat world string 3;7,220*1,5*3,2;3;,biome_1

                with open(mission_file, 'r') as xmlFile:
                        self.missionXML = xmlFile.read()
        
                # Create default Malmo objects:

                self.agent_host = MalmoPython.AgentHost()
                try:
                        self.agent_host.parse( sys.argv )
                except RuntimeError as e:
                        print 'ERROR:',e
                        print self.agent_host.getUsage()
                        exit(1)
                if self.agent_host.receivedArgument("help"):
                        print self.agent_host.getUsage()
                        exit(0)
                        
        def start(self):
                self.malmo_mission = MalmoPython.MissionSpec(self.missionXML, True)
                self.malmo_mission_record = MalmoPython.MissionRecordSpec()

                self.malmo_mission.requestVideo(800, 500)
                self.malmo_mission.setViewpoint(1)

                # Attempt to start a mission:
                max_retries = 3
                for retry in range(max_retries):
                        try:
                                self.agent_host.startMission(self.malmo_mission, self.malmo_mission_record )
                                break
                        except RuntimeError as e:
                                if retry == max_retries - 1:
                                        print "Error starting mission:",e
                                        exit(1)
                                else:
                                        time.sleep(2)

                # Loop until mission starts:
                print "Waiting for the mission to start ",
                self.world_state = self.agent_host.getWorldState()
                while not self.world_state.has_mission_begun:
                        #sys.stdout.write(".")
                        time.sleep(0.1)
                        self.world_state = self.agent_host.getWorldState()
                        for error in self.world_state.errors:
                                print "Error:",error.text

                print
                print "Mission running ",
                
        def is_running(self):
                return self.world_state.is_mission_running
                
        def get_observation(self):
                '''
                loads floor grid, edge distances, and current player cell
                '''
                edges = ["Top", "Right", "Bottom", "Left"]
                while self.world_state.is_mission_running:
                        #sys.stdout.write(".")
                        time.sleep(0.1)
                        self.world_state = self.agent_host.getWorldState()
                        if len(self.world_state.errors) > 0:
                                raise AssertionError('Could not load grid.')

                        if self.world_state.number_of_observations_since_last_state > 0:
                                msg = self.world_state.observations[-1].text
                                state = json.loads(msg)
                        
                                grid = state.get(u'floorAll', 0)
                                distances = [state.get(u'distanceFrom' + e, 0) for e in edges]
                                cell = state.get(u'cell', 0)
                        
                                self.agent_location = cell
                                break
                                
                return observation(grid, distances, cell)
                
        def send_command(self, cmd):
                if self.agent_location not in self.blocks_traveled:
                        self.blocks_traveled[self.agent_location] = 0
                self.blocks_traveled[self.agent_location] += 1
                print ("Agent traveled at location " + str(self.agent_location))
                self.agent_host.sendCommand(cmd)
                
        def check_errors(self):
                self.world_state = self.agent_host.getWorldState()
                for error in self.world_state.errors:
                        print "Error:",error.text
                        
        def block_score(self):
                score = 0
                for location in self.blocks_traveled:
                        score += math.log(self.blocks_traveled[location] + 1, 2) # diminishing returns for being at the same block
                        
                return score
