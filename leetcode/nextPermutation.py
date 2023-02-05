class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=len(nums)-1
        while j>0 and nums[j-1]>=nums[j]:
            j-=1
        if j>0:
            i=j-1
            k=len(nums)-1
            while k>=j:
                if nums[k]<=nums[i]:
                    k-=1
                else:
                    temp = nums[k]
                    nums[k] = nums[i]
                    nums[i]=temp
                    break
            i+=1
            j=len(nums)-1
            while i<j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j]=temp
                j-=1
                i+=1
        else:
            nums.reverse()