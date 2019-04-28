import pytest
from pytest import raises
from simplemaths.simplemaths import SimpleMaths as sm
import math

class TestSimpleMaths():
    @pytest.mark.parametrize('input', [5, 10, 500])
    def testInitPos(self, input):
        TestInit = sm(input)
        assert TestInit.number == input

    @pytest.mark.parametrize('input', [5.0, '5', None])
    def testInitNeg(self, input):
        with raises(TypeError):
            sm(input)
    
    @pytest.mark.parametrize('input', [5, 10, 500])
    def testSquare(self, input):
        TestInit = sm(input)
        assert TestInit.square() == input**2 
    
    @pytest.mark.parametrize('input', [1, 10, 500])
    def testFactorial(self, input):
        TestInit = sm(input)
        if input == 0:
            assert TestInit.factorial() == 1
        else:
            assert TestInit.factorial() == math.factorial(input)
    
    @pytest.mark.parametrize("input, power", [(5, 1) , (10, 2), (500, 3)])
    def testPower(self, input, power):
        TestInit = sm(input)
        assert TestInit.power(power) == input ** power

    @pytest.mark.parametrize("input, oe", [(5, 'Odd') , (10, 'Even'), (500, 'Even')])
    def testOddOrEven(self, input, oe):
        TestInit = sm(input)
        assert TestInit.odd_or_even() == oe
    
    @pytest.mark.parametrize("input, sqrt", [(1, 1) , (4, 2), (10, math.sqrt(10))])
    def testSqrt(self, input, sqrt):
        TestInit = sm(input)
        assert math.isclose(TestInit.square_root(), sqrt, rel_tol=1e-9, abs_tol=0.0)
