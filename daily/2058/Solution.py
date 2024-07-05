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
    
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        
        # Quantidade de nós insuficiente
        if not(head and head.next and head.next.next): return [-1,-1]

        prev = head
        actual = head.next
        post = head.next.next
        criticalPoints = []
        pos = 2

        # Analisa se 'actual' é local minima ou maxima
        # Se for, coloca em 'criticalPoints' a posição dele
        while post:
            if actual.val > prev.val and actual.val > post.val:
                # local maxima
                criticalPoints.append(pos)
            elif actual.val < prev.val and actual.val < post.val:
                # local minima
                criticalPoints.append(pos)
            pos += 1
            prev = actual
            actual = post
            post = post.next

        # Quantidade de pontos críticos insuficiente
        if len(criticalPoints) < 2: return [-1,-1]

        # A máxima distância é obviamente a maior posição menos a menor
        # A menor distância INICIA com o mesmo valor, já que qualquer outra distância será menor
        minDistance = maxDistance = criticalPoints[-1] - criticalPoints[0]

        # Verifica em pares qual a menor distância
        # Se achar 1, já é a menor possível e para o loop
        i = 1
        while i < len(criticalPoints) and minDistance != 1:
            minDistance = min(minDistance,  criticalPoints[i] - criticalPoints[i-1])
            i += 1

        return [minDistance, maxDistance]