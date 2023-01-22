class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        st = set(nums)
        ls =[]
        dic = {}
        for i in st:
            dic[i]=nums.count(i)
        for i in range (k):
            _max = max(dic, key=dic.get)
            ls.append(_max)
            dic[_max]=-1
        return ls