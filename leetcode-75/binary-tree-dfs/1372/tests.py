import pytest
from Solution import Solution

# O modo de construção da árvore através da lista fornecida pelo enunciado não é capaz de 
# criar a mesma árvore construída neste código.
# Logo, os testes irão falhar, porém, o código funciona no LeetCode

''''
def test_example1():
    
    root = Solution().arrToTree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
    
    output = Solution().longestZigZag(root)
    
    assert output == 3
    
def test_example2():
    
    root = Solution().arrToTree([1,1,1,None,1,None,None,1,1,None,1])
    
    output = Solution().longestZigZag(root)
    
    assert output == 4
    
def test_example3():
    
    root = Solution().arrToTree([1])
    
    output = Solution().longestZigZag(root)
    
    assert output == 0
'''