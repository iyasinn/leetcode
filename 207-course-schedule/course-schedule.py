"""
We have numCourses labed from 0 to n - 1
adn for each of them, we have a rpreq requeste 
We can do a topo sort for this 

might not need the topo sort
just need to see if we hit something that is already visited

So lets say we start a multi source bfs 
And we start from all the courses
And now two courses hit a course, that is actually okay if the source is diff

But if the source


Fro graph problems, create an adjacency list or an adjacency matrix

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        inDegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj[prereq].append(course)
            inDegree[course] += 1
        
        visited = 0
        bfs = [i for i in range(len(inDegree)) if inDegree[i] == 0]

        while bfs: 
            node = bfs.pop(0)
            visited += 1

            for other in adj[node]:
                inDegree[other] -= 1
                if inDegree[other] == 0:
                    bfs.append(other)
        
        return visited == numCourses


        


        
        