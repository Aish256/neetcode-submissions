class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair up position and speed, sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []  # stores time-to-reach-target for each fleet
        
        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)
            # if current car reaches target no later than the car ahead (top of stack),
            # it merges into that fleet — so pop it off
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)