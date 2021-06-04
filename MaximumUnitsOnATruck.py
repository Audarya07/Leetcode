class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        res = 0
        
        for cnt, units in boxTypes:
            if truckSize > 0:
                if cnt < truckSize:
                    res += (cnt * units)
                else:
                    res += (truckSize * units)
            truckSize -= cnt

                    
        return res
            