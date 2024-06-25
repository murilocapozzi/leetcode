import pytest
from Solution import Solution

# Estão comentados os 'asserts' com resposta do LeetCode pois
# não é dada a transformação de lista para TreeNode e vice-versa que nos fornece
# logo, criei a minha própria então o resultado final é diferente, porém a árvore é a mesma
# apenas impressa de forma INFIXA, enquanto que do exercício é por nível


def test_example1():

    nums = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    
    root = Solution().transform(nums) # Lista para TreeNode

    root = Solution().bstToGst(root) # Atualiza os valores de root
    
    root = root.transform(root) # TreeNode para Lista

    assert root == [30, 36, 36, None, None, 35, None, 33, None, None, 21, 26, None, None, 15, None, 8, None, None]
    #assert root == [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]

def test_example2():

    nums = [0,None,1]
    
    root = Solution().transform(nums) # Lista para TreeNode

    root = Solution().bstToGst(root) # Atualiza os valores de root
    
    root = root.transform(root) # TreeNode para Lista

    assert root == [1, None, 1, None, None]
    #assert root == [1,None,1]