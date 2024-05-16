import pytest

def my_function(x: int) -> int:
    if not isinstance(x, int):
        raise ValueError("variável precisa ser numérica!")    
    return x * 2

def test_my_funtion_returns_double_the_input():
    actual_result = my_function(x=5)
    
    assert actual_result == 10
    
def test_my_function_raises_when_x_is_not_int():
    with pytest.raises(ValueError):
        my_function(x="texto")
        
    with pytest.raises(ValueError):
        my_function(x="2342.323")
        

print(my_function(4))
print(my_function('5'))
print(my_function('A'))

