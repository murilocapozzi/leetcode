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
    
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # currentHead irá manter onde está o primeiro zero da sequência em análise
        # Este zero irá se tornar o nó unido, a soma dos próximos não-nulos
        currentHead = head
        p = head.next

        # O enunciado garante que o primeiro e o último elemento são zeros
        # então algumas verificações são descartadas

        while p.next:

            currentSum = 0

            # Acumula soma até encontrar outro zero
            while p.val != 0:
                currentSum += p.val
                p = p.next

            # Encontrado o zero, atualiza a currentHead
            # e ela apontará agora para p, ou seja, remove todos não-nulos entre currentHead e p
            # Após isso, currentHead progride e reinicia o loop sendo novamente o primeiro zero
            # Se p.next for None, currentHead irá apontar direto para None e o loop principal quebra
            currentHead.val = currentSum
            if p.next:
                currentHead.next = p
                currentHead = currentHead.next
                p = p.next
            else:
                currentHead.next = None

        return head