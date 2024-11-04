class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            inDegree[course] += 1
        

        bfs = [i for i in range(len(inDegree)) if inDegree[i] == 0]
        i = 0

        while i < len(bfs): 
            node = bfs[i]

            for other in adj[node]:
                inDegree[other] -= 1
                if inDegree[other] == 0:
                    bfs.append(other)
            i += 1
        
        return bfs if len(bfs) == numCourses else []


        
