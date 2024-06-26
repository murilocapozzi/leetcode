from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def arrToList(self, arr):
        head = None
        
        for i in range(len(arr)-1, -1, -1): head = ListNode(val=arr[i], next=head)
        
        return head
        
    def listToArr(self, head):
        arr = []
        
        p = head
        while p:
            arr.append(p.val)
            p = p.next
            
        return arr
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Mantém a lista original e retorna uma nova, reversa

        new = None
        p = head

        while p:
            new = ListNode(val=p.val, next=new)
            p = p.next

        return new