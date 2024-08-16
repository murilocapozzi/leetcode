import pytest
from Solution import KthLargest



def test_example1():

    k = 3
    nums = [4, 5, 8, 2]
    newNums = [3, 5, 10, 9, 4]
    
    obj = KthLargest(k, nums)
    
    output = [None]
    
    for num in newNums:
        
        kThNum = obj.add(num)
        output.append(kThNum)

    assert output == [None, 4, 5, 5, 8, 8]