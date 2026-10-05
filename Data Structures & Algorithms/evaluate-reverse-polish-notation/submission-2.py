class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            try:
                val = int(t)
                stack.append(val)
                
            except ValueError:
                v2 = stack.pop()
                v1 = stack.pop()

                if t == "+":
                    stack.append(int(v1 + v2))
                if t == "-":
                    stack.append(int(v1 - v2))
                if t == "*":
                    stack.append(int(v1 * v2))
                if t == "/":
                    stack.append(int(v1 / v2))
                
        
        return int(stack.pop())