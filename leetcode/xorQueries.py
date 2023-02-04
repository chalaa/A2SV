class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ls = []
        ls.append(arr[0])
        fin=[]
        for i in range(1,len(arr)):
            ls.append(ls[i-1] ^ arr[i])
        for j in range(len(queries)):
            lf,rh= queries[j]
            if lf==rh:
                fin.append(arr[lf])
            elif lf==0:
                fin.append(ls[rh])
            else:
                fin.append(ls[rh]^ls[lf]^arr[lf])
        return fin