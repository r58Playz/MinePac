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
                    <Placement x="0" y="56" z="0" yaw="-90"/>
                </AgentStart>
                <AgentHandlers>
                  <DiscreteMovementCommands/>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                  <ChatCommands/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

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
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission running ",

#spawn mobs using chat command
#agent_host.sendCommand("chat /summon Zombie 24 56 0")

# Loop until mission ends:
while world_state.is_mission_running:
    sys.stdout.write(".")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print "Error:",error.text

print
print "Mission ended"
# Mission has ended.
