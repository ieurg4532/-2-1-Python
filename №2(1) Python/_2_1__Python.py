import math
from mod import Fibonacci

def expression(x):
    if x > 45:
        z = -(math.sqrt(x))
    elif x<= 45:
        z = math.sin(2*x)
    return z 
"""
def Fibonacci(p):
    F0, F1 = 1, 1
    while F1 <= p:
        F0, F1 = F1, F0 + F1
    return F1
"""

x = int(input("Введіть число x: "))
print("Значення виразу z = ", expression(x))

p = int(input("Введіть число p: "))
print("Перше число Фібоначчі, що більше заданого числа р = ",Fibonacci(p))