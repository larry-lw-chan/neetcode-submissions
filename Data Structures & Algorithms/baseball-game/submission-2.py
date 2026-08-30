class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # create a stack to hold record
        stack = []

        # Iterate through instruction set
        for operation in operations:
            top_idx = len(stack) - 1

            # + = Record new score that's sum previous two scores
            if operation == '+':
                res = stack[top_idx] + stack[top_idx - 1]
                stack.append(res)

            # D =  Record new score that's double of previous scores
            elif operation == 'D':
                res = stack[top_idx] * 2
                stack.append(res)

            # C = Invalidate previous score
            elif operation == 'C':
                stack.pop()

            # Else append number to stack if core
            else:
                stack.append(int(operation))

        # Add all numbers in stack and calculate result
        result = 0
        for num in stack:
            result += int(num)

        # return result
        return result
                

                

            
