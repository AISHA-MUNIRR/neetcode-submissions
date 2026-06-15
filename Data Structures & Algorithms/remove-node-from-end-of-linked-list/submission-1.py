# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        size=0
        while curr!=None:
            curr=curr.next
            size=size+1

        if size==1:
            return None

        if n==size:
            return head.next
        
        curr=head
        index=size-n
        i=1
        while i<index:
            curr=curr.next
            i+=1
        curr.next=curr.next.next

        return head
