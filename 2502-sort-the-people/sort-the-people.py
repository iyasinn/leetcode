class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        same = [(heights[i], names[i]) for i in range(len(names))]
        same.sort(reverse=True)
        return [x[1] for x in same]
