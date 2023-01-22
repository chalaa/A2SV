class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        for i in s:
            if(len(ls)==0):
                ls.append(i)
            elif(i=="(" or i=="{"or i=="[" ):
                ls.append(i)
            else:
                if(i==")" and ls[-1]=="("):
                    ls.pop()
                elif(i=="]" and ls[-1]=="["):
                    ls.pop()
                elif(i=="}" and ls[-1]=="{"):
                    ls.pop()
                else:
                    ls.append(i)
        if(len(ls)>0):
            return False
        else: 
            return True