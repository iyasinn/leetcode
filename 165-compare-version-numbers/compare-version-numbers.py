class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        # maxLen = max(len(v1), len(v2))
      
        # v1 += (maxLen - len(v1)) * ["0"]
        # v2 += (maxLen - len(v2)) * ["0"]
        # print(v1)
        # print(v2)

        for i in range(max(len(v1), len(v2))):
            if (i >= len(v1) and int(v2[i]) > 0): 
                return -1
            elif (i >= len(v2) and int(v1[i]) > 0): 
                return 1
            elif (i < len(v1) and i < len(v2)): 
                if int(v1[i]) < int(v2[i]): 
                    return -1
                elif int(v1[i]) > int(v2[i]): 
                    return 1
        
        return 0