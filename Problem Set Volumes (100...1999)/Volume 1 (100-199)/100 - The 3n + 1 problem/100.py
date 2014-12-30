#!/usr/bin/env python

def problem(n):
    i = 1
    while n > 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        i = i + 1
    return i

def get_max_interval(i, j):
    min = 0
    max = 0
    if i > j:
        i, j = j, i
    for x in range(i,j):
        min = problem(x)
        if max < min:
            max = min
    return max

if __name__ == '__main__':
    while True:
        try:
            a, b = map(int, raw_input().split())
            if a > 0 and b > 0:
                print "%d %d %d" % (a, b, get_max_interval(a,b))
        except ValueError, EOFError:
            break
