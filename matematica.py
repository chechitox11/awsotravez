"""
Your module description
"""
def sumar(x,y):
    return x+y
def primo(x):
    if x<2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True