from main import area_calculation
import pytest
from pytest import fixture, mark

@fixture(autouse=True)
def set_up():
    print("Start test")

class TestArea:

#    @mark.usefixtures("set_up")
    def test_one(self):
        s_one, s_two, year = area_calculation(1, 5)
        assert s_one == 4
        assert s_two == 45
        assert year == 3

    def test_two(self):
        result = area_calculation(" ", 5)
        assert result == "Error"

    @mark.parametrize('a,b,result', ([" ", " ", "Error"],
                                       [None, None, "Error"],
                                       ["234", "321", "Error"],
                                       [1.12, 2.45, "Error"]))
    def test_three(self, a, b, result):
        res = area_calculation(a, b)
        assert result == res, "Error"

    @mark.parametrize('a, b, r1, r2, r3', ([1, 5, 4, 45, 3],
                                           [1, 1, 64, 729, 7]))
    def test_four(self, a, b, r1, r2, r3):
        res1, res2, res3 = area_calculation(a, b)
        assert res1 == r1
        assert res2 == r2
        assert res3 == r3