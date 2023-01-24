class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while(len(stack)!=0 and stack[-1]==popped[0]):
                stack.pop()
                popped.pop(0)
        if(len(stack)==0):
            return True
        return False