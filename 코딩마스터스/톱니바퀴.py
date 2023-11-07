# -*- coding: utf-8 -*-
import sys
from math import ceil
a, b, c = map(int, sys.stdin.readline().split())

k = 10*c/a

print(ceil(k))