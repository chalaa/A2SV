class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        ls=[]
        nums.sort()
        while(i<j):
            ls.append(nums[i]+nums[j])
            i+=1
            j-=1
        return(max(ls))