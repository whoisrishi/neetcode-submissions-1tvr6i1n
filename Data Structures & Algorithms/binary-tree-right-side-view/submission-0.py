class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        q = [root]

        while q:
            res.append(q[-1].val)

            for _ in range(len(q)):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res