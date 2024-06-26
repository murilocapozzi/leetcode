import pytest
from Solution import Solution


def test_example1():
    
    senate = "RD"
    
    output = Solution().predictPartyVictory(senate)
        
    assert output == 'Radiant'
    
def test_example2():
    
    senate = "RDD"
    
    output = Solution().predictPartyVictory(senate)
        
    assert output == 'Dire'