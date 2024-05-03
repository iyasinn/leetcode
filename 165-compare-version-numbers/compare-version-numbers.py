class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1 += max(len(v2) - len(v1), 0) * ["0"]
        v2 += max(len(v1) - len(v2), 0) * ["0"]

        print(v1)
        print(v2)

        for a, b in zip(v1, v2):
            if int(a) < int(b): 
                return -1
            elif int(a) > int(b): 
                return 1
        
        return 0