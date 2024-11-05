# id, type, element
def parse(s):
    s = s.split(":")
    return int(s[0]), s[1], int(s[2])

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0] * n
        stack = []

        for log in logs:
            _id, _type, _time = parse(log)
            if _type == "end":
                output[_id] += ((_time) - stack[-1][2]) + 1
                stack.pop()
                if stack:
                    stack[-1] = (stack[-1][0], stack[-1][1], _time + 1)
            elif _type == "start":
                if stack:
                    output[stack[-1][0]] += (_time - stack[-1][2])
                stack.append((_id, _type, _time))
        
        return output



        



        