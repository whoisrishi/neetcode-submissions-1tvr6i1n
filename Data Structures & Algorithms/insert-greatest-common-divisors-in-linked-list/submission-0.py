class Solution:
    def insertGreatestCommonDivisors(self, head):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        cur = head
        while cur and cur.next:
            cur.next = ListNode(gcd(cur.val, cur.next.val), cur.next)
            cur = cur.next.next
        return head