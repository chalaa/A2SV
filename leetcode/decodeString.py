class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        stack_num =[]
        num=""
        st=""
        for i in range(len(s)):
            if s[i].isdigit():
                num+=s[i]
            elif s[i]=="[":
                stack_num.append(int(num))
                num=""
                stack.append(s[i])
            elif s[i]=="]":
                print(stack)
                while not stack[-1] == "[":
                    ss=stack.pop()
                    st = ss+st
                stack.pop()
                num_t =stack_num.pop()
                st=st*num_t
                stack.append(st)
                st=""
                
            else:
                stack.append(s[i])
        for j in stack:
            st+=j
        return st