import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([4,2,7,1,3])
    val = 2
    
    output = Solution().treeToArr(Solution().searchBST(root, val))
    
    assert output == [2, 1, 3]
    
def test_example2():
    
    root = Solution().arrToTree([4,2,7,1,3])
    val = 5
    
    output = Solution().treeToArr(Solution().searchBST(root, val))
    
    assert output == []