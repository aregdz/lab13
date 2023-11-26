#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_before_last_positive(*args):
   if args:
        l = 0
        for i, u in enumerate(args):
            if u > 0:
                l = i

        return sum(args[:l])

   else:
       return None

if __name__ == '__main__':
    p = list(int(i) for i in input("Введите значения: ").split())
    result = sum_before_last_positive(*p)
    print(result)