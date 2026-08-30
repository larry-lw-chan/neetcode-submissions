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

                # Do Logic
                last_idx = len(stack) - 1

                # Logic for ')'
                if c == ')':
                    if stack[last_idx] == '(':
                        stack.pop()
                    else:
                        return False

                elif c == '}':
                    if stack[last_idx] == '{':
                        stack.pop()
                    else:
                        return False        

                elif c == ']':                
                    if stack[last_idx] == '[':
                        stack.pop()
                    else:
                        return False

        # If no closing found
        if len(stack) == 0:
            return True
        else:
            return False


