from time import sleep

def add(x):
    return x + 1


def test_should_pass():
    sleep(3)
    assert add(3) == 4


def test_should_fail():
    sleep(3)
    assert add(4) == 3
