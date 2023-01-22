import math
n,m,a = [int(i) for i in input().split()]
w=math.ceil(n/a)
l=math.ceil(m/a)
print(w*l)