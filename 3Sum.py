# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


# Brute force solution will be O(N^3) --> 3 nested for loop i, j and k 
# to check every triplet



# TC - O(N^2) --> optimal solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    val = [nums[i], nums[l], nums[r]]
                    res.append(val)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return resclass Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        # sort the array
        nums.sort()
        
        for i in range(n-2):
            # proceed if no duplicates found adjacent to each other
            if i == 0 or nums[i] != nums[i-1]:
                l = i+1
                h = n-1
                
                while l < h:
                    if nums[l] + nums[h] + nums[i] == 0:
                        res.append([nums[i], nums[l], nums[h]])
                        # after a triplet is found, if the next element
                        # is duplicate the skip it
                        while l < h and nums[l] == nums[l+1]:
                            l += 1
                        while l < h and nums[h] == nums[h-1]:
                            h -= 1
                        # currently you are on duplicate element
                        # move 1 more step to reach next valid element 
                        # after skipping the duplicates
                        l += 1
                        h -= 1
                        
                    elif nums[l] + nums[h] + nums[i] < 0:
                        l += 1
                        
                    else:
                        h -= 1
        return res
