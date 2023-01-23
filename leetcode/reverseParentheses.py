class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = s
        ls=[]
        for i in range(len(s)):
            if(s[i]=="("):
                ls.append(i)
            elif(s[i]==")"):
                ind = ls.pop()
                st= st[:ind] + st[ind:i+1][::-1]+st[i+1::]
        st = st.replace("(","")
        st = st.replace(")","")
        return st