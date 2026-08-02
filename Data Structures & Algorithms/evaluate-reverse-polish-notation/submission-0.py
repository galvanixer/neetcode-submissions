class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def applyoperation(self, t1:int, t2:int, op:str) -> int:
            if op == "+":
                return t1+t2
            elif op == "-":
                return t1-t2
            elif op == "*":
                return t1*t2
            elif op == "/":
                return int(t1/t2)

        stack = []
        op = ""
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else: 
                t2 = stack.pop()
                t1 = stack.pop()
                stack.append(applyoperation(self, t1, t2, t))

        return stack.pop()
        