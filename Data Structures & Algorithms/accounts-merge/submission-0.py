class Solution:
    def accountsMerge(self, accounts):
        parent = list(range(len(accounts)))
        rank = [0] * len(accounts)
        email_to_id = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return

            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email] = i

        merged = {}

        for email, i in email_to_id.items():
            root = find(i)
            if root not in merged:
                merged[root] = []
            merged[root].append(email)

        result = []

        for root, emails in merged.items():
            result.append([accounts[root][0]] + sorted(emails))

        return result