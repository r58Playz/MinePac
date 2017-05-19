---
layout:	default
title:	Proposal
---

## Summary

This project will teach an agent to explore and survive in a contained but hostile environment. The agent will be able omniscient, knowing the contents of every voxel in the environment, but will have to learn to succeed in the environment using genetic, hill-climbing, reinforcement learning, and other local search algorithms. These algorithms will take the world state as input, and output a list of movement commands designed to maximize the agent's exploration and survival. By comparing the success of these algorithms, this project will provide an empirical measure of their suitability for tasks in this domain.

## Algorithms

This project will deploy and compare genetic, hill-climbing, reinforcement learning, and other local search algorithms.

## Evaluation Plan

Each algorithm will be evaluated both on agent performance, and on the time it takes the algorithm to achieve that performance. Experience points will be scattered around the environment, and the algorithms will attempt to maximize the number of experience points the agent gains. This metric encourages both survival and exploration. If the agent dies before it has the opportunity to gather all available experience points, its performance will be lower than that of an agent that survives longer. However, if the agent attempts to maximize survival time by staying in the same place, it will be unable to collect experience points scattered throughout the environment. The algorithms will be compared with each other both by the maximum performance they are able to achieve, and by the number of iterations it takes for the algorithm to reach that level of performance.

Ideally, each algorithm should produce a sequence of movement commands that causes the agent to gather experience points while avoiding obstacles and hazards. The environments should be sufficiently challenging and complex that different algorithms come up with different approaches, and that safely navigating the environment is nontrivial. Finally, the comparisons between the algorithms should be sufficiently robust that they provide clear evidence of their relative strengths and weaknesses. If some algorithms, for example, optimize agent behavior more quickly but have a tendency to get stuck on local minima, while other algorithms achieve better performance but require more iterations, these differences should be apparent in our comparative measurements.

## Appointment
An appointment has been scheduled for May 1st at 3:15pm.

**Note:** This proposal is preliminary. Details may be subject to change as the project progresses.
