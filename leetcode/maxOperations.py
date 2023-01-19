class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ct=0
        i=0
        j=len(nums)-1
        while(i<j and len(nums)>0):
            if(nums[i]+nums[j] == k):
                ct = ct+1
                nums.pop(j)
                nums.pop(i)
                j=j-2
            elif(nums[i]+nums[j] > k):
                j=j-1
            else:
                i=i+1
        return ct