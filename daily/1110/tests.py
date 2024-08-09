import pytest
from Solution import Solution



def test_example1():
    
    root = Solution().arrToTree([1,2,3,4,5,6,7])
    to_delete = [3,5]
    
    output = Solution().delNodes(root, to_delete)
    ans = [[], [], []]
    Solution().treeToArr(output[0], ans[0], 0)
    Solution().treeToArr(output[1], ans[1], 0)
    Solution().treeToArr(output[2], ans[2], 0)
    
    while ans[0][-1] == None: ans[0].pop()
    while ans[1][-1] == None: ans[1].pop()
    while ans[2][-1] == None: ans[2].pop()
    
    assert ans[0] == [1,2,None,4]
    assert ans[1] == [6]
    assert ans[2] == [7]
    
def test_example2():
    
    root = Solution().arrToTree([1,2,4,None,3])
    to_delete = [3]
    
    output = Solution().delNodes(root, to_delete)
    ans = [[]]
    Solution().treeToArr(output[0], ans[0], 0)
    
    while ans[0][-1] == None: ans[0].pop()
    
    assert ans[0] == [1,2,4]