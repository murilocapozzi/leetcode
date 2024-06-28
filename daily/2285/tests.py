import pytest
from Solution import Solution

# Estão comentados os 'asserts' com resposta do LeetCode pois
# não é dada a transformação de lista para TreeNode e vice-versa que nos fornece
# logo, criei a minha própria então o resultado final é diferente, porém a árvore é a mesma
# apenas impressa de forma INFIXA, enquanto que do exercício é por nível


def test_example1():

    n = 5
    roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    
    output = Solution().maximumImportance(n, roads)
    
    assert output == 43

def test_example2():

    n = 5
    roads = [[0,3],[2,4],[1,3]]
    
    output = Solution().maximumImportance(n, roads)
    
    assert output == 20
    
def test_example3():
    
    n = 5
    roads = [[0,1]]
    
    output = Solution().maximumImportance(n, roads)
    
    assert output == 9