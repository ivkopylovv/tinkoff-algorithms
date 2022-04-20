from math import sqrt


def time(x):
    return sqrt(pow(a, 2) + pow(1 - x, 2)) / vf + sqrt(pow(x, 2) + pow(1 - a, 2)) / vp


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


vp, vf = map(int, input().split())
a = float(input())

left = 0
right = 1

while (right - left >= 0.00000001):

    f = left + (right - left) / 3
    g = right - (right - left) / 3

    if time(f) < time(g):
        right = g
    else:
        left = f

print(toFixed(left, 7))
