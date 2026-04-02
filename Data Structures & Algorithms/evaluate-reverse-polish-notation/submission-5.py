class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        if len(tokens) < 2: 
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(b - a)
                elif tokens[i] == '/':
                    stack.append(int(b / a))
                elif tokens[i] == '*':
                    stack.append(a * b)
        
        return stack[-1]    

        # 2 +1  = 3
        # 3 * 3 = 9 
        # 9,4 