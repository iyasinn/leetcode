class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+', '-', '/', '*']

        for element in tokens:
            if element not in operators:
                stack.append(element)
            else:
                secondNum = int(stack.pop())
                firstNum = int(stack.pop())
                match element:
                    case "+":
                        val = firstNum + secondNum
                    case "-":
                        val = firstNum - secondNum
                    case "/":
                        val = firstNum / secondNum
                    case "*":
                        val = firstNum * secondNum
                stack.append(val)
        return int(stack[0])