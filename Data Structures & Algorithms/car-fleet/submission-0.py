class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Figure IF a car can pass/catch-up to another car, before target.
        # Store by [position2: time to reach, position1: time to reach]
        # Since all position from [-1] will get lower, only keep the SLOWEST time to reach.
        # This ensure cars behind it CAN catch up.

        # [12, 3, 7, 1, 1]
        # [5, 2.6, 6]


        timeToReach = list()

        for i in range(len(position)):
            pos = position[i]
            sp = speed[i]

            ttr = (target-pos)/sp
            timeToReach.append([pos, ttr])

        timeToReach = sorted(timeToReach, key=lambda x: x[0])

        slowestTime = float('-inf')
        fleet = 0

        while(len(timeToReach) > 0):
            currTime = timeToReach.pop()[1]

            if (currTime > slowestTime):
                slowestTime = currTime
                fleet += 1

        return fleet






            


