import pytest
from Solution import RecentCounter


def test_example():
    
    obj = RecentCounter()
    result = [None]
    times = [1, 100, 3001, 3002]
    
    for t in times:
        numRequests = obj.ping(t)
        result.append(numRequests)
        
    assert result ==[None, 1, 2, 3, 3]