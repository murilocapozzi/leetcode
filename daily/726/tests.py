import pytest
from Solution import Solution



def test_example1():

    formula = "H2O"

    output = Solution().countOfAtoms(formula)

    assert output == "H2O"

def test_example2():

    formula = "Mg(OH)2"

    output = Solution().countOfAtoms(formula)

    assert output == "H2MgO2"
    
def test_example2():

    formula = "K4(ON(SO3)2)2"

    output = Solution().countOfAtoms(formula)

    assert output == "K4N2O14S4"