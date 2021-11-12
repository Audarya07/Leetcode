class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for val in s:
            # if opening brackets found, put in stack
            if val in d:
                stack.append(val)
            # if stack not empty and closing bracket found, check if pair matches
            elif stack and val == d[stack[-1]]:
                stack.pop()
            # no opening brackets found till now
            else:
                return False
        # if stack empty --> return True, else return False
        return len(stack) == 0
