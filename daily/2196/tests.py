import pytest
from Solution import Solution



def test_example1():
    
    descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    
    output = []
    Solution().treeToArr(Solution().createBinaryTree(descriptions), output, 0)
        
    while output[-1] == None:
        output.pop()
        
    assert output == [50,20,80,15,17,19]
    
def test_example2():
    
    descriptions = [[1,2,1],[2,3,0],[3,4,1]]
    
    output = []
    Solution().treeToArr(Solution().createBinaryTree(descriptions), output, 0)
    
    while output[-1] == None:
        output.pop()
        
    assert output == [1,2,None,None,3,4]