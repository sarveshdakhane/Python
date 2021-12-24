class Evaluation:
    def __init__(self) -> None:
        self.stack=[]
    def isEmpty (self):
        return self.stack ==[]
    def Push (self,op):
        self.stack.append(op)
    def Pop (self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return '$'

    def EvalutePostFix(self,exp):
        for c in exp:
            if c.isdigit():
                self.Push(c)
            else:
                a =self.Pop()
                b= self.Pop()
                self.Push(str(eval(b+c+a)))
        return int(self.Pop())


e= Evaluation()
print(e.EvalutePostFix('234*6*+'))