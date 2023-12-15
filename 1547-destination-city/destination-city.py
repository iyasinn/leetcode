class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list(set(x[1] for x in paths).difference([x[0] for x in paths]))[0]
        