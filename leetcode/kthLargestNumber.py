class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ls = [int(i) for i in nums]
        ls.sort(reverse=True)
        st = str(ls[k-1])
        return st
