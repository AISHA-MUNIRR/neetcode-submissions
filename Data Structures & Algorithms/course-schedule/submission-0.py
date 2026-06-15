class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap= {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        
        visitedset=set()

        def dfs(crs):

            if crs in visitedset:
                return False
            if premap[crs]==[]:
                return True

            visitedset.add(crs)

            for pre in premap[crs]:
                if not dfs(pre): return False
            premap[crs]=[]
            visitedset.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i): 
                return False
        return True





