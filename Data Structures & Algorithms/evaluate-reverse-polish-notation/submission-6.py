class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # > Brute Force Solution. Time: O(n^2), Space: O(n)
        ALLOWED_OPERATIONS = {"+", "-", "*", "/"}
        while len(tokens)>1:
            for (i,t) in enumerate(tokens):
                if t in ALLOWED_OPERATIONS:
                    a, b = int(tokens[i-1]), int(tokens[i-2])
                    if t == "+":
                        res = b + a
                    elif t == "-":
                        res = b - a
                    elif t == "*":
                        res = b * a
                    elif t== "/":
                        res = int(b/a)

                    tokens = tokens[:i-2]+[str(res)]+tokens[i+1:]
                    break

        return int(tokens[0])


        # # > Optimal Solution. Time: O(n) , Space: O(n)
        # ALLOWED_OPERATIONS = {"+", "-", "*", "/"}
        # stack = []
        # for t in tokens:
        #     if t in ALLOWED_OPERATIONS and len(stack)>=2:
        #         a, b = stack.pop(), stack.pop()
        #         if t == "+":
        #             stack.append(b+a)
        #         elif t == "-":
        #             stack.append(b-a)
        #         elif t == "*":
        #             stack.append(b*a)
        #         elif t == "/":
        #             stack.append(int(b/a))
        #     else:
        #         stack.append(int(t))

        # return stack.pop()




































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
        