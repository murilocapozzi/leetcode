import pytest
from Solution import Solution

# Estão comentados os 'asserts' com resposta do LeetCode pois
# não é dada a transformação de lista para TreeNode e vice-versa que nos fornece
# logo, criei a minha própria então o resultado final é diferente, porém a árvore é a mesma


def test_example1():

    root = [1,None,2,None,3,None,4,None,None]

    root = Solution().balanceBST(root)
    listRoot = root.transform(root)

    assert listRoot == [2,1,3,4] or listRoot == [3,1,4,2]
    #assert root == [2,1,3,null,null,null,4] or root == [3,1,4,null,2]

def test_example2():

    root = [2,1,3]

    root = Solution().balanceBST(root)
    listRoot = root.transform(root)

    assert listRoot == [2,1,3]
    #assert root == [2,1,3]