class Solution:
    def buildTree(self, preorder, inorder):
        pos = {v: i for i, v in enumerate(inorder)}
        pre = 0

        def dfs(l, r):
            nonlocal pre
            if l > r:
                return None

            root = TreeNode(preorder[pre])
            mid = pos[preorder[pre]]
            pre += 1

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)