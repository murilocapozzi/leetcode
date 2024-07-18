import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([1,2,3,None,4])
    distance = 3
    
    output = Solution().countPairs(root, distance)
        
    assert output == 1
    
def test_example2():
    
    root = Solution().arrToTree([1,2,3,4,5,6,7])
    distance = 3
    
    output = Solution().countPairs(root, distance)
        
    assert output == 2
    
def test_example3():
    
    root = Solution().arrToTree([7,1,4,6,None,5,3,None,None,None,None,None,2])
    distance = 3
    
    output = Solution().countPairs(root, distance)
        
    assert output == 1