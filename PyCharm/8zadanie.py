#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def sredgeom(*a):
    if a:
        n = len(a)
        y = 1
        for i in a:
            y *= i

        s = math.pow(y,1/n)
        return s

    else:
        return None

if __name__ == "__main__":
    p = list(int(i) for i in input("Введите значения: ").split())
    result = sredgeom(*p)
    print(result)