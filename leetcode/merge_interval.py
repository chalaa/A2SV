class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ls = []
        for i in intervals:
            if(len(ls)==0):
                ls.append(i)
            else:
                ls1 = ls[-1]
                if(i[0]>=ls1[0] and i[0]<=ls1[1]):
                    if(i[1]>ls1[1]):
                        ls1[1] = i[1]
                else:
                    ls.append(i)
        return ls