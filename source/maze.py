# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #2: Run simple mission using raw XML

import MalmoPython
import os
import sys
import time
import json
import random

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

# More interesting generator string: "3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"
# flat world string 3;7,220*1,5*3,2;3;,biome_1

missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Hello world!</Summary>
              </About>
              
              <ServerSection>
                <ServerInitialConditions>
                    <Time>
                        <StartTime>20000</StartTime>
                        <AllowPassageOfTime>false</AllowPassageOfTime>
                    </Time>
                </ServerInitialConditions>

                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;35;village"/>
                  <DrawingDecorator>
                      <DrawCuboid x1="0" x2="27" y1="55" y2="55" z1="-14" z2="16" type="glowstone"/>
                      <DrawCuboid x1="0" x2="0" y1="55" y2="55" z1="-14" z2="16" type="air"/>
                      <DrawCuboid x1="27" x2="27" y1="55" y2="55" z1="-14" z2="16" type="air"/>
                      <DrawCuboid x1="0" x2="27" y1="55" y2="55" z1="-14" z2="-14" type="air"/>
                      <DrawCuboid x1="0" x2="27" y1="55" y2="55" z1="16" z2="16" type="air"/>
                      <DrawBlock x="0" y="55" z="0" type="glowstone"/>
                      <DrawBlock x="27" y="55" z="0" type="glowstone"/>
                      <DrawCuboid x1="2" x2="5" y1="55" y2="55" z1="-10" z2="-12" type="air"/>
                      <DrawCuboid x1="7" x2="11" y1="55" y2="55" z1="-10" z2="-12" type="air"/>
                      <DrawCuboid x1="13" x2="14" y1="55" y2="55" z1="-10" z2="-13" type="air"/>
                      <DrawCuboid x1="16" x2="20" y1="55" y2="55" z1="-10" z2="-12" type="air"/>
                      <DrawCuboid x1="22" x2="25" y1="55" y2="55" z1="-10" z2="-12" type="air"/>
                      <DrawCuboid x1="2" x2="5" y1="55" y2="55" z1="-7" z2="-8" type="air"/>
                      <DrawCuboid x1="7" x2="8" y1="55" y2="55" z1="-1" z2="-8" type="air"/>
                      <DrawCuboid x1="9" x2="11" y1="55" y2="55" z1="-4" z2="-5" type="air"/>
                      <DrawCuboid x1="10" x2="17" y1="55" y2="55" z1="-7" z2="-8" type="air"/>
                      <DrawCuboid x1="13" x2="14" y1="55" y2="55" z1="-4" z2="-6" type="air"/>
                      <DrawCuboid x1="19" x2="20" y1="55" y2="55" z1="-1" z2="-8" type="air"/>
                      <DrawCuboid x1="16" x2="18" y1="55" y2="55" z1="-4" z2="-5" type="air"/>
                      <DrawCuboid x1="22" x2="25" y1="55" y2="55" z1="-7" z2="-8" type="air"/>
                      <DrawCuboid x1="0" x2="5" y1="55" y2="55" z1="-1" z2="-5" type="air"/>
                      <DrawCuboid x1="22" x2="26" y1="55" y2="55" z1="-1" z2="-5" type="air"/>
                      <DrawCuboid x1="10" x2="17" y1="55" y2="55" z1="-2" z2="2" type="air"/>
                      <DrawCuboid x1="0" x2="5" y1="55" y2="55" z1="1" z2="5" type="air"/>
                      <DrawCuboid x1="22" x2="26" y1="55" y2="55" z1="1" z2="5" type="air"/>
                      <DrawCuboid x1="7" x2="8" y1="55" y2="55" z1="1" z2="5" type="air"/>
                      <DrawCuboid x1="19" x2="20" y1="55" y2="55" z1="1" z2="5" type="air"/>
                      <DrawCuboid x1="10" x2="17" y1="55" y2="55" z1="4" z2="5" type="air"/>
                      <DrawCuboid x1="13" x2="14" y1="55" y2="55" z1="6" z2="8" type="air"/>
                      <DrawCuboid x1="2" x2="5" y1="55" y2="55" z1="7" z2="8" type="air"/>
                      <DrawCuboid x1="4" x2="5" y1="55" y2="55" z1="9" z2="11" type="air"/>
                      <DrawCuboid x1="22" x2="25" y1="55" y2="55" z1="7" z2="8" type="air"/>
                      <DrawCuboid x1="22" x2="23" y1="55" y2="55" z1="9" z2="11" type="air"/>
                      <DrawCuboid x1="1" x2="2" y1="55" y2="55" z1="10" z2="11" type="air"/>
                      <DrawCuboid x1="25" x2="26" y1="55" y2="55" z1="10" z2="11" type="air"/>
                      <DrawCuboid x1="2" x2="11" y1="55" y2="55" z1="13" z2="14" type="air"/>
                      <DrawCuboid x1="7" x2="8" y1="55" y2="55" z1="10" z2="12" type="air"/>
                      <DrawCuboid x1="16" x2="25" y1="55" y2="55" z1="13" z2="14" type="air"/>
                      <DrawCuboid x1="19" x2="20" y1="55" y2="55" z1="10" z2="12" type="air"/>
                      <DrawCuboid x1="2" x2="11" y1="55" y2="55" z1="13" z2="14" type="air"/>
                      <DrawCuboid x1="7" x2="11" y1="55" y2="55" z1="7" z2="8" type="air"/>
                      <DrawCuboid x1="16" x2="20" y1="55" y2="55" z1="7" z2="8" type="air"/>
                      <DrawCuboid x1="10" x2="17" y1="55" y2="55" z1="10" z2="11" type="air"/>
                      <DrawCuboid x1="13" x2="14" y1="55" y2="55" z1="11" z2="14" type="air"/>
                      <DrawCuboid x1="0" x2="27" y1="54" y2="54" z1="-14" z2="16" type="lava"/>
                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="30000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>PacManBot</Name>
                <AgentStart>
                    <Placement x="0.5" y="56" z="0.5" yaw="-90"/>
                </AgentStart>
                <AgentHandlers>
                  <DiscreteMovementCommands/>
                  <ChatCommands/>
                  <ObservationFromGrid>
                      <Grid name="floorAll">
                        <min x="-1" y="-1" z="-1"/>
                        <max x="1" y="-1" z="1"/>
                      </Grid>
                  </ObservationFromGrid>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''


def load_grid(world_state):
    '''
    loads floor grid
    '''
    while world_state.is_mission_running:
        #sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load grid.')

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            observations = json.loads(msg)
            grid = observations.get(u'floorAll', 0)
            break
    return grid

def at_junction(grid):
    '''
    checks if agent is at a junction given the floor grid
    '''
    if(grid[1] == u'glowstone' or grid[7] == u'glowstone'):
        return grid[3] == u'glowstone' or grid[5] == u'glowstone'
    if(grid[3] == u'glowstone' or grid[5] == u'glowstone'):
        return grid[1] == u'glowstone' or grid[7] == u'glowstone'

    #this will probably never get called
    #return true just to allow policy evaluation if it does get called
    #may change this later
    return true

def random_policy(grid):
    '''
    grid is
        0 1 2
        3 4 5
        6 7 8
    '''
    actions_list = []
    if(grid[1] == u'glowstone'):
        actions_list.append('movenorth 1')
    if(grid[3] == u'glowstone'):
        actions_list.append('movewest 1')
    if(grid[5] == u'glowstone'):
        actions_list.append('moveeast 1')
    if(grid[7] == u'glowstone'):
        actions_list.append('movesouth 1')
    
    r = random.random()
    a = random.randint(0, len(actions_list) - 1)
    return actions_list[a]


# Create default Malmo objects:

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print 'ERROR:',e
    print agent_host.getUsage()
    exit(1)
if agent_host.receivedArgument("help"):
    print agent_host.getUsage()
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

my_mission.requestVideo(800, 500)
my_mission.setViewpoint(1)

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print "Error starting mission:",e
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print "Waiting for the mission to start ",
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    #sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission running ",

#spawn mobs using chat command
#agent_host.sendCommand("chat /summon Zombie 24 56 0")

#initialize action
action = ''

# Loop until mission ends:
while world_state.is_mission_running:
    #sys.stdout.write(".")
    time.sleep(0.1)

    #agent performs movement action here
    grid = load_grid(world_state)
    if(action == '' or at_junction(grid)):
        action = random_policy(grid)
    print
    print action
    agent_host.sendCommand(action)
    #the sleep time determines how fast the agent moves
    time.sleep(0.3)
    
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission ended"
# Mission has ended.
