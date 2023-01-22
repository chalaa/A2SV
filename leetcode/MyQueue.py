class MyQueue:

    def __init__(self):
        self.ls=[]

    def push(self, x: int) -> None:
        self.ls.append(x)

    def pop(self) -> int:
        return self.ls.pop(0)

    def peek(self) -> int:
        return self.ls[0]

    def empty(self) -> bool:
        if(len(self.ls)==0):
            return True
        else:
            return False