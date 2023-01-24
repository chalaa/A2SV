class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=-1
        prev_max =-1
        i=0
        j=len(height)-1
        while(i<j):
            h=min(height[i],height[j])
            w=j-i
            max_area = max(max_area,h*w)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_area