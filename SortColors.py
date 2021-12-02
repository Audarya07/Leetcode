# Naive approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one  = 0
        two = 0
        
        for val in nums:
            if val == 0:
                zero += 1
            elif val == 1:
                one += 1
            else:
                 two += 1
        
        x = 0
        for i in range(zero):
            nums[x] = 0
            x += 1
        for i in range(one):
            nums[x] = 1
            x += 1
        for i in range(two):
            nums[x] = 2
            x += 1


# One pass solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # red = 0, white = 1, blue = 2

        red, white = 0, 0
        blue = len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
        return nums
                