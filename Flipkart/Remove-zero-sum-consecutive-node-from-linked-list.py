from collections import OrderedDict
ListNode=[]
def removeZeroSumSublists(head):
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next