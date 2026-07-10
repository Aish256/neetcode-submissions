class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    # Using int(left / right) handles truncation toward zero 
                    # for both positive and negative results in Python.
                    stack.append(int(left / right))
                    
        return stack[0]
