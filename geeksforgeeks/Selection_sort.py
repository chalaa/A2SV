class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min_val = self.select(arr,i)
            for j in range(n):
                if(arr[j]>min_val):
                    min_val = arr[j]
                    arr[j]=arr[i]
                    arr[i] = min_val
        return arr