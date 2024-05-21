class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ['+', '-', '/', '*']

        for element in tokens:
            if element not in operators:
                stack.append(int(element))
            else:
                secondNum = stack.pop()
                firstNum = stack.pop()
                match element:
                    case "+":
                        val = firstNum + secondNum
                    case "-":
                        val = firstNum - secondNum
                    case "/":
                        val = firstNum / secondNum
                    case "*":
                        val = firstNum * secondNum
                stack.append(int(val))
        return int(stack[0])