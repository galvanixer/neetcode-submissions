class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        # > Optimal Solution. Time: , Space: 
        ALLOWED_OPERATIONS = {"+", "-", "*", "/"}
        stack = []
        for t in tokens:
            if t in ALLOWED_OPERATIONS and len(stack)>=2:
                a, b = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(b+a)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(b*a)
                elif t == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(t))

        return stack.pop()




































        # stack = []
        # operationset = {"+", "-", "*", "/"}
        # for t in tokens:
        #     if t not in operationset:
        #         stack.append(int(t))
        #     else: 
        #         t2 = stack.pop()
        #         t1 = stack.pop()
        #         if t == "+":
        #             stack.append(t1+t2)
        #         elif t == "-":
        #             stack.append(t1-t2)
        #         elif t == "*":
        #             stack.append(t1*t2)
        #         else: 
        #             stack.append(int(t1/t2))

        # return stack.pop()
        