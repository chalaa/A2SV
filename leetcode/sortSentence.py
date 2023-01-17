class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        ss = ""
        s=s.split()
        for x in s:
            d[int(x[-1])] = x[:-1]
        for i in range(1,len(s)+1):
            ss = ss + d[i] +" "
        ss=ss.strip()
        return ss