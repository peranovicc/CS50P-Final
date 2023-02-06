from generated_module import get_minimum

def test_group1():
    assert get_minimum([1, 2, 3, 4, 5]) == 1
    assert get_minimum([1, 2, 3, 4, 5, 232, -1, 232, 2]) == -1

def test_hidden1():
    assert get_minimum([]) == None
    assert get_minimum([1]) == 1

def test_hidden2():
    assert get_minimum([1,1,1]) == 1
    assert get_minimum([0,-1,1]) == -1
    assert get_minimum([99,22,3,66]) == 3

