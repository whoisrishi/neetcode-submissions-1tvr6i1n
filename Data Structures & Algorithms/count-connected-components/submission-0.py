class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        count = n

        for a, b in edges:
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                if rank[rootA] < rank[rootB]:
                    rootA, rootB = rootB, rootA

                parent[rootB] = rootA
                rank[rootA] += rank[rootB]
                count -= 1

        return count