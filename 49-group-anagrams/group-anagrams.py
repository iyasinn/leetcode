class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs: 
            key = "".join(sorted(word))
            groups[key] = groups.get(key, [])
            groups[key].append(word)
            
        return groups.values()