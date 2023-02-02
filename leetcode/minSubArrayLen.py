class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ls=[]
        sum=nums[0]
        i=0
        j=1
        while i<j:
            if sum>=target:
                ls.append(j-i)
                sum-=nums[i]
                i+=1
            else:
                if j<len(nums):
                    sum+=nums[j]
                    j+=1
                if j==len(nums) and sum<target:
                    break
        if len(ls) >0:
            return min(ls)
        return 0