class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        av = k*threshold
        sum=0
        for i in range(k):
            sum+=arr[i]
        ct=0
        if sum>=av:
            ct+=1
        i=0
        j=k
        while j<len(arr):
            sum = sum+arr[j]-arr[i]
            if sum>=av:
                ct+=1
            j+=1
            i+=1
        return ct 