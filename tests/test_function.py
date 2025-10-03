from exercise.function_task import *


def test_function():
    assert function_1(3, 4) == 12
    assert function_2(1) == False
    assert function_3(6) == [1, 2, 3, 6]
    assert function_4(5) == [0, 1, 1, 2, 3]
    
