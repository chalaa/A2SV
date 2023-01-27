class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        prevpro=-1
        ls=[]
        for i in range(len(nums)):
            if i==0 or nums[i]==0:
                for j in range(len(nums)):
                    if i!=j and nums[j] ==0:
                        pro=0
                        break
                    if i!=j:
                        pro*=nums[j]
                ls.append(pro)
                pro=1
            else:
                pro=(ls[-1]//nums[i])*nums[i-1]
                ls.append(pro)
                pro=1
        return ls