class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                if(nums[i]==nums[j]):
                    c = c+1
        return c