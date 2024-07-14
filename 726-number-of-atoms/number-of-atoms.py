
def isOneQuantity(items, index): 
    return index + 1 >= len(items) or not items[index + 1].isnumeric()

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        simple = [formula[0]]

        for i in range(1, len(formula)):
            char = formula[i]
            if simple[-1][0].isupper() and char.islower(): 
                simple[-1] += char 
            elif simple[-1][0].isnumeric() and char.isnumeric(): 
                simple[-1] += char
            else:
                simple += [char]
        
        p = []
        event = {}

        for i in range(len(simple)): 
            if simple[i] == "(": 
                p.append(i)
                pass
            elif simple[i] == ")":
                count = 1 if isOneQuantity(simple, i) else int(simple[i + 1])
                event[p[-1]] = count
                event[i] = count
                p.pop()

        # print(simple)
        # print(event)

        freq = {}
        mult = 1

        for i in range(len(simple)): 
            
            if simple[i].isalpha(): 
                count = 1 if isOneQuantity(simple, i) else int(simple[i + 1])
                freq[simple[i]] = freq.get(simple[i], 0) + (count * mult)
            elif simple[i] == "(": 
                mult *= event[i]
            elif simple[i] == ")":
                mult = mult // event[i]
        
        solution = ""
        for key in sorted(freq.keys()): 
            solution += str(key) + (str(freq[key]) if freq[key] > 1 else "")
        return solution

        # multiplier = 1 
        # counts = {}

        # events = {}

        # for i in range(len(formula)): 
        #     if events[i] == "(": 
                
        