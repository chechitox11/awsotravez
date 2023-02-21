"""
Your module description
"""
from matematica import sumar, primo

def test_sumar():
    assert sumar(2,3)==5
    assert sumar(2,2)==4
    assert sumar(1,2)==3
    
def test_primo():
    assert primo(3) is True
    assert primo(2) is True
    assert primo(10) is False
    assert primo(8) is False