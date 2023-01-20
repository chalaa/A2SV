class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ct=0
        n=len(piles)//3
        piles.sort()
        for i in range(n):
            piles.pop(-1)
            ct = ct + piles[-1]
            piles.pop(-1)
        return ct