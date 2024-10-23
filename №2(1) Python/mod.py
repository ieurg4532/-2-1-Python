def Fibonacci(p):
    F0, F1 = 1, 1
    while F1 <= p:
        F0, F1 = F1, F0 + F1
    return F1
