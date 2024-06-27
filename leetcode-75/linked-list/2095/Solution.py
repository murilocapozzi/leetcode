

# Definition for singly-linked list.
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
    
    def deleteMiddle(self, head):
        
        length = 0
        p = head
        
        # Descobre o tamanho da lista
        while p:
            length += 1
            p = p.next
            
        mid = (length // 2)
        
        i = 0
        p = head
        prev = None
        
        # Descobre qual elemento é o do meio
        while p.next and i != mid:
            prev = p
            p = p.next
            i += 1
        
        # Arruma ponteiros
        if prev:
            prev.next = p.next
            
        # Exclui o elemento do meio
        p = None
        
        return head