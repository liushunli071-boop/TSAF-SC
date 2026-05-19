import math

def f(x):
    return sum(x) / len(x)

def g(x):
    mean = sum(x) / len(x)
    return sum((xi - mean) ** 2 for xi in x) / len(x)

def h(x):
    return sum(1 for xi in x if xi < 0) / len(x)

def sigma(x, alpha=0.4, beta=0.4, gamma=0.2):
    return alpha * f(x) + beta * g(x) + gamma * h(x)