def getCount(items, index):
    if index + 1 >= len(items) or not items[index + 1].isnumeric(): 
        return 1
    return int(items[index + 1])

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        reduced = [formula[0]]
        
        # Not too necessary
        for i in range(1, len(formula)):
            char = formula[i]
            if reduced[-1][0].isupper() and char.islower(): 
                reduced[-1] += char 
            elif reduced[-1][0].isnumeric() and char.isnumeric(): 
                reduced[-1] += char
            else:
                reduced += [char]
        
        stack = []
        event = {}
        
        # Capture multipliers
        for i in range(len(reduced)): 
            if reduced[i] == "(": 
                stack.append(i)
            elif reduced[i] == ")":
                event[stack[-1]] = getCount(reduced, i)
                event[i] = getCount(reduced, i)
                stack.pop()

        freq = {}
        mult = 1
        
        # Capture frequencies
        for i in range(len(reduced)): 
            if reduced[i].isalpha(): 
                count = getCount(reduced, i)
                freq[reduced[i]] = freq.get(reduced[i], 0) + (count * mult)
            elif reduced[i] == "(": 
                mult *= event[i]
            elif reduced[i] == ")":
                mult = mult // event[i]
        
        # Gen solution
        solution = ""
        for key in sorted(freq.keys()): 
            solution += str(key) + (str(freq[key]) if freq[key] > 1 else "")

        return solution