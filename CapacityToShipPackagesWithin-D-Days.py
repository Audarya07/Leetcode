class Solution:
    def shipWithinDays(self, wt: List[int], days: int) -> int:
        l = max(wt)
        r = sum(wt)

        while l < r:
            m = (l+r)//2
            
            num_ship = 1
            curr_cap = 0
            for w in wt:
                curr_cap += w
                if curr_cap > m:
                    curr_cap = w
                    num_ship += 1
                    
            if num_ship > days:
                l = m + 1
            else:
                r = m
                
        return l          
                
# Solution:
# https://www.youtube.com/watch?v=1w4-rZhP7BM