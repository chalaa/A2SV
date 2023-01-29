class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rig_sum=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            rig_sum-=nums[i]
            if rig_sum== left_sum:
                return i
            left_sum+=nums[i]
        return -1