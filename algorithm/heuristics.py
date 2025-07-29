import sys
import random

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    A = [[0] * n for _ in range(n)]
    for _ in range(m):
        i, j, w = map(int, sys.stdin.readline().split())
        A[i][j] += w
        if i != j:
            A[j][i] += w
    return n, A

def calc_score(x, A):
    s = 0
    n = len(x)
    for i in range(n):
        if x[i]:
            s += A[i][i]
            for j in range(i+1, n):
                if x[j]:
                    s += 2 * A[i][j]
    return s

def calc_gain(i, x, A):
    delta = A[i][i] * (1 if x[i] == 0 else -1)
    for j in range(len(x)):
        if i != j and x[j]:
            delta += 2 * A[i][j] * (1 if x[i] == 0 else -1)
    return delta

def greedy_init(n, A):
    x = [0] * n
    candidates = [(A[i][i], i) for i in range(n)]
    candidates.sort(reverse=True)
    for _, i in candidates:
        gain = calc_gain(i, x, A)
        if gain > 0:
            x[i] = 1
    return x

def multi_pass_local_search(x, A, passes=5):
    for _ in range(passes):
        improved = False
        for i in range(len(x)):
            gain = calc_gain(i, x, A)
            if gain > 0:
                x[i] ^= 1
                improved = True
        if not improved:
            break
    return x

def main():
    n, A = read_input()
    best_x = greedy_init(n, A)
    best_x = multi_pass_local_search(best_x, A, passes=5)
    print(' '.join(map(str, best_x)))

if __name__ == "__main__":
    main()