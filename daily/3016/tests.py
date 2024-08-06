import pytest
from Solution import Solution



def test_example1():
    
    word = "abcde"
    
    output = Solution().minimumPushes(word)
        
    assert output == 5
    
def test_example2():
    
    word = "xyzxyzxyzxyz"
    
    output = Solution().minimumPushes(word)
        
    assert output == 12
    
def test_example3():
    
    word = "aabbccddeeffgghhiiiiii"
    
    output = Solution().minimumPushes(word)
        
    assert output == 24