import pytest
from Solution import Solution

# O enunciado compara os resultados pela própria classe
# Para adequar, modifiquei para comparar com o valor do nó, já que são únicos
# Está comentado em Solution a solução submetida ao LeetCode

def test_example1():
    
    root = Solution().arrToTree([3,5,1,6,2,0,8,None,None,7,4])
    p = 5
    q = 1
    
    output = Solution().lowestCommonAncestor(root, p, q)
    
    assert output == 3
    
def test_example2():
    
    root = Solution().arrToTree([3,5,1,6,2,0,8,None,None,7,4])
    p = 5
    q = 4
    
    output = Solution().lowestCommonAncestor(root, p, q)
    
    assert output == 5
    
def test_example3():
    
    root = Solution().arrToTree([1,2])
    p = 1
    q = 2
    
    output = Solution().lowestCommonAncestor(root, p, q)
    
    assert output == 1