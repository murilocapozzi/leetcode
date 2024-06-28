

# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
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
    
    def breakListInTwo(self, head):
    # Adaptado do problema #2095 Delete the Middle Node of a Linked List
    # Quebra a head em duas metades
    
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
            
        mid = (length // 2)
        i = 0
        p = head
        prev = None
        while p.next and i != mid:
            prev = p
            p = p.next
            i += 1
        
        if prev: prev.next = None
        
        return [head, p]
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Função usada no problema #206 Reverse Linked List
    # Inverte a ordem da segunda metade
    
        new = None
        p = head

        while p:
            new = ListNode(val=p.val, next=new)
            p = p.next

        return new
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        head, half = self.breakListInTwo(head)
        half = self.reverseList(half)
        
        p = head
        q = half
        maxSum = 0
        
        # Percorre as duas metades somando o valor e retornando o máximo
        while p and q:
            twinSum = p.val + q.val
            maxSum = max(maxSum, twinSum)
            p = p.next
            q = q.next
            
        return maxSum