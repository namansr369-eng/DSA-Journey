# 134. Gas Station
# Medium

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
# You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel
# around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution,
# it is guaranteed to be unique.


from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        total_gas_tank = 0  # Used for the overall feasibility check
        current_tank = 0    # Used for the current trip attempt
        start_index = 0     # The potential starting station index
        
        for i in range(n):
            
            net_gain = gas[i] - cost[i]
            total_gas_tank += net_gain
            current_tank += net_gain
            
            if current_tank < 0:
                current_tank = 0
                start_index = i + 1
        
        if total_gas_tank >= 0:
            return start_index
        else:
            return -1