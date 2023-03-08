import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot

########################Problem1########################


def calculate(a, b, oper):
    if oper == "+":
        print(a + b)
    elif oper == "-":
        print(a - b)
    elif oper == "*":
        print(a * b)
    elif oper == "/":
        if a==0 or b==0:
            print("TRY AGAIN")
            problem_1()
            return 0
        else:
            print(a // b, a % b, "(remainder)")
    else:
        print("TRY AGAIN")
        problem_1()
        return 0


def problem_1():
    print("INPUT1")
    a = int(input())
    print("INPUT2")
    b = int(input())
    print("OPERATOR")
    operator = input()
    calculate(a, b, operator)


problem_1()
print("\n\n\n")

########################Problem2########################


# Generate array
def gen():
    arr = np.random.randint(0, 10, size=100).reshape(10, 10)
    bas = np.arange(0, 10)
    zeros = np.zeros(10, dtype="int")
    res = []
    dict2 = dict(zip(bas, zeros))
    for _ in arr:
        dict1 = dict(zip(bas, zeros))
        for k in _:
            dict1[k] += 1
            dict2[k] += 1
        res.append(dict1)
    return bas, arr, res


# DataFrame
def dataframe(bas, res):
    df = pd.DataFrame(res, index=bas + 1)
    print(df)
    print("\n")


# Histogram1: each frequency
def histogram1(arr):
    fig, axes = plt.subplots(2, 5, constrained_layout=True, sharex="all", sharey="all")
    pyplot.xlim([0, 9])
    pyplot.ylim([0, 10])
    r = np.array([0] * 5 + [1] * 5)
    c = np.array([np.arange(5)] * 2).reshape(-1)
    idx = [[r[i], c[i]] for i in range(10)]

    k = 0
    for n, m in idx:
        axes[n][m].hist(arr[k], bins=10)
        axes[n][m].set_title("number" + str(k))
        axes[n][m].grid()
        k += 1

    plt.show()

# Histogram2: frequency
def histogram2(arr):
    arr = np.reshape(arr, -1)
    print(arr)
    plt.hist(arr, histtype='bar')
    plt.grid(True, axis='y')
    plt.show()

basic, array, result = gen()
dataframe(basic, result)
histogram2(array)
print("\n\n\n")

########################Problem3########################


def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2, 0, -1):
        max_heapify(arr, i, n)


def max_heapify(arr, i, n):
    l = 2*i
    r = 2*i + 1
    if l < n and arr[l] > arr[i]:
        largest = l
    else :
        largest = i
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)


def heapsort(arr):
    build_max_heap(arr)
    n = len(arr)
    for k in range(n-1, 1, -1):
        arr[1], arr[k] = arr[k], arr[1]
        max_heapify(arr, 1, k)


arr = [0] + list(np.random.randint(1, 1000, size=1000))
print("ORIGINAL")
print(arr)

heapsort(arr)
arr.pop(0)
print("SORTED")
print(arr)

