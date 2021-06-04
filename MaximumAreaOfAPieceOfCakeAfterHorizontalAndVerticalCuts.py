class Solution:
    def maxArea(self, h: int, w: int, h_cuts: List[int], v_cuts: List[int]) -> int:
        MOD = (10**9)+7
        h_cuts.sort()
        v_cuts.sort()
        
        # Horizontal cuts
        # Each horizontal cut will give height of the piece of cake
        h_size = [h_cuts[0]]
        for i in range(1, len(h_cuts)):
            h_size.append(h_cuts[i] - h_cuts[i-1])
        h_size.append(h - h_cuts[len(h_cuts)-1])
        
        
        # Vertical cuts
        # Each vertical cut will give width of the piece of cake
        v_size = [v_cuts[0]]
        for i in range(1, len(v_cuts)):
            v_size.append(v_cuts[i] - v_cuts[i-1])
        v_size.append(w - v_cuts[len(v_cuts)-1])
        
        max_h = max(h_size)
        max_w = max(v_size)
        
        return (max_h*max_w)%MOD