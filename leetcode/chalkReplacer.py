class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        ls=[]
        sum=0
        fla=False
        for i in range(len(chalk)):
            sum+=chalk[i]
            ls.append(sum)
        x=k//ls[-1]
        k=k-(ls[-1]*x)
        for i in range(len(ls)):
            if ls[i] > k:
                break
        return i