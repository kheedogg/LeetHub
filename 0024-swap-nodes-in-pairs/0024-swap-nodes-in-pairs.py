# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        ans = node
        while head and head.next != None:
            # switch head.val and head.next.val 
            tmp = ListNode(head.val)
            tmp_node = head.next
            tmp2 = ListNode(tmp_node.val)
            tmp2.next = tmp
            
            node.next = tmp2
            node = tmp
            head = tmp_node.next
        
        if head:
            node.next = head
        return ans.next