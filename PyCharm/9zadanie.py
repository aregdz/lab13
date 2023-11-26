#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sredgeom(*a):
    if a:
        n = len(a)
        y = 0
        for i in a:
            y += 1/i
        return n/y

    else:
        return None


if __name__ == "__main__":
    p = list(int(i) for i in input("Введите значения: ").split())
    result = sredgeom(*p)
    print(result)