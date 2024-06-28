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
    
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Tempo: O(N) -- percorre apenas uma vez
        # Espaço: O(1) -- cria-se apenas ponteiros para os nós
        
        # Se a lista possui tamanho 1 ou 2, já está correto
        if not head or not head.next: return head

        # Ponteiro que irá percorrer na (odd)head
        odd = head
        
        # Cria uma segunda cabeça, que irá manter os pares (even)
        evenHead = head.next

        # Ponteiro que irá percorrer na evenHead
        even = evenHead


        # Percorre a head e troca aos pares os ponteiros
        # O próximo do odd insere na even
        # O próximo do even insere no odd
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next


        # Ao final, concatena evenHead no final da odd
        odd.next = evenHead

        return head