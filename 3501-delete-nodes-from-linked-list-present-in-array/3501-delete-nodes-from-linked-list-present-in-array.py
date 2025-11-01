# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_uniq = set(nums)

        node = head
        prev_node = None
        while node != None:
            if node.val in nums_uniq: # 제거해야하는 상황
                if prev_node == None: # 이전 노드가 없는 경우
                    head = node.next
                    node = node.next
                else: # 이전 노드가 있는 경우 
                    prev_node.next = node.next
                    node = node.next
            else:
                prev_node = node
                node = node.next

        return head

