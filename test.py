import time

def add(a, b):
    return a + b

def executeTime():
    start_time = time.time()
    result = add(5, 10)
    end_time = time.time()
    print(f"Result: {result}, Execution Time: {end_time - start_time} seconds")

def test_add():
    assert add(5, 10) == 15
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -10) == -15

def test_executeTime():
    start_time = time.time()
    executeTime()
    end_time = time.time()
    assert end_time - start_time <
