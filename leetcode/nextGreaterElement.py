class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        for i in range(len(nums1)):
            ind = nums2.index(nums1[i])
            ma=-1
            for j in range(ind,len(nums2)):
                if nums2[j]>nums1[i]:
                    ma = nums2[j]
                    break
            stack.append(ma)
        return stack