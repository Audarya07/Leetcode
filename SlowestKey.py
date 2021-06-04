class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        temp = [0]*len(releaseTimes)
        temp[0] = releaseTimes[0]
        
        for i in range(1, len(releaseTimes)):
            temp[i] = releaseTimes[i] - releaseTimes[i-1]
                
        mx = 0
        index = 0
        for idx, val in enumerate(temp):
            if val > mx:
                mx = val
                index = idx
            if val == mx:
                if keysPressed[idx] > keysPressed[index]:
                    index = idx
                
        return keysPressed[index]