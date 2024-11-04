class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj[prereq].append(course)
            inDegree[course] += 1
        
        visited = 0
        bfs = [i for i in range(len(inDegree)) if inDegree[i] == 0]
        i = 0

        while i < len(bfs): 
            node = bfs[i]
            visited += 1

            for other in adj[node]:
                inDegree[other] -= 1
                if inDegree[other] == 0:
                    bfs.append(other)
            i += 1
        
        if visited != numCourses:
            return []

        return bfs[::-1]


        
