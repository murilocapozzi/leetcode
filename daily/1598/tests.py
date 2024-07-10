import pytest
from Solution import Solution



def test_example1():

    logs = ["d1/","d2/","../","d21/","./"]

    output = Solution().minOperations(logs)

    assert output == 2

def test_example2():

    logs = ["d1/","d2/","./","d3/","../","d31/"]

    output = Solution().minOperations(logs)

    assert output == 3
    
def test_example2():

    logs = ["d1/","../","../","../"]

    output = Solution().minOperations(logs)

    assert output == 0