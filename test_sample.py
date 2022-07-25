from time import sleep
from pytest_testrail.plugin import pytestrail


def add(x):
    return x + 1

@pytestrail.case('C2253')
def test_should_pass():
    sleep(3)
    assert add(3) == 4

@pytestrail.case('C2252')
def test_should_fail():
    sleep(3)
    assert add(4) == 3
