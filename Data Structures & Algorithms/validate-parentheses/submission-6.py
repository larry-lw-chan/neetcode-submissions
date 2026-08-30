class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack
        stack = []

        # Iterate through string
        for c in s:
            # Append if opening brackets
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            
            # Do comparision
            else:
                # Edge Case Handling
                if len(stack) == 0: return False

                # Look for corresponding brackets
                if c == ')':
                    if stack[len(stack) - 1] == '(':
                        stack.pop()
                    else:
                        return False

                elif c == '}':
                    if stack[len(stack) - 1] == '{':
                        stack.pop()
                    else:
                        return False        

                elif c == ']':                
                    if stack[len(stack) - 1] == '[':
                        stack.pop()
                    else:
                        return False

        # Return true if stack is empty, else return false
        if len(stack) == 0: return True
        return False


