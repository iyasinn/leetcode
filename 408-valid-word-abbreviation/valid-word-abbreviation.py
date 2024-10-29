

def getNext(wordRef):
    if len(wordRef) == 0:
        return None, None
    
    isnum = wordRef[0].isnumeric()
    output = []

    while len(wordRef) > 0:
        nextChar = wordRef[0]
        if nextChar.isnumeric() ^ isnum:
            break
        output.append(nextChar)
        wordRef.pop(0)
    
    if isnum:
        val = "".join(output)
        if len(val) != len(str(int(val))) or int(val) == 0:
            return None, None
        return int, int("".join(output))
    else:
        return str, "".join(output)

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    
        abbr = list(abbr)

        while abbr:
            dataType, data = getNext(abbr)
            
            if dataType == str:
                if len(word) < len(data) or word[0:len(data)] != data:
                    return False
                word = word[len(data)::]
            elif dataType == int:
                if len(word) < data:
                    return False
                word = word[data::]
            else:
                return False
    
        if len(word) > 0:
            return False
            
        return True


        