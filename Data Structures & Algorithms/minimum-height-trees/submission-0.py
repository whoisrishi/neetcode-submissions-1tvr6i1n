class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adj = [set() for _ in range(n)]
        degree = [0] * n

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

        leaves = [i for i in range(n) if degree[i] == 1]
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves