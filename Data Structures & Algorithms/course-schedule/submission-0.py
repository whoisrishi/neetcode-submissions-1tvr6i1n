class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        path = set()

        def dfs(course):
            if course in path:
                return False
            if not graph[course]:
                return True

            path.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True