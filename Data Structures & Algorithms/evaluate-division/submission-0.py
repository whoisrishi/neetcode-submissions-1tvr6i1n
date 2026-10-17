class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), v in zip(equations, values):
            graph.setdefault(a, []).append((b, v))
            graph.setdefault(b, []).append((a, 1 / v))

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for nei, val in graph[src]:
                if nei not in visited:
                    res = dfs(nei, dst, visited)
                    if res != -1.0:
                        return val * res

            return -1.0

        ans = []

        for a, b in queries:
            ans.append(dfs(a, b, set()))

        return ans