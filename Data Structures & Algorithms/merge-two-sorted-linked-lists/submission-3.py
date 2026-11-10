# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            head = list1
            first = list1.next
            sec = list2
        else:
            head = list2
            first = list1
            sec = list2.next

        tail = head

        while first and sec:

            if first.val <= sec.val:
                tail.next = first
                first = first.next
            else:
                tail.next = sec
                sec = sec.next

            tail = tail.next

        if first:
            tail.next = first
        else:
            tail.next = sec

        return head




















        