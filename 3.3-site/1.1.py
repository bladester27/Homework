from concurrent.futures import ThreadPoolExecutor
from math import prod as p
from time import time as t
import threading


def fact(arg1, arg2):
    for _ in range(arg1, arg2 + 1):
        results.append(_)


results = []
with ThreadPoolExecutor(max_workers=2) as executor:
    result = executor.map(fact, )
    print(result)