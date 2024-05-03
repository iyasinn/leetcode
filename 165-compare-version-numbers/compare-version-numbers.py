class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        maxLen = max(len(v1), len(v2))
        # v1, v2 = (v2, v1) if len(v1) > len(v2) else (v1, v2)
        v1 += (maxLen - len(v1)) * ["0"]
        v2 += (maxLen - len(v2)) * ["0"]
        print(v1)
        print(v2)

        for a, b in zip(v1, v2):
            if int(a) < int(b): 
                return -1
            elif int(a) > int(b):
                return 1
        


        return 0