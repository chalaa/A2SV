class Solution:
    def fib(self, n: int) -> int:
        f0=0
        f1=1
        f2 =1
        if n==0:
            return f0
        elif n==1:
            return f1
        elif n==2:
            return f2
        else:
            for i in range (n-2):
                temp = f1
                f1 = f2
                f2 = f1+temp
            return f2