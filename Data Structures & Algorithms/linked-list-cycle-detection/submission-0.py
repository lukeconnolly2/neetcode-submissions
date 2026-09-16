# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None
        while fast is not None:
            if fast == slow:
                return True
            slow = slow.next if slow else None
            fast = fast.next if fast else None            
            fast = fast.next if fast else None            

        return False