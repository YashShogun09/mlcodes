import math

def ab_prune(d, i, is_max, v, a, b, md):
    if d == md: return v[i]
    if is_max:
        for j in range(2):
            a = max(a, ab_prune(d+1, i*2+j, False, v, a, b, md))
            if b <= a: break
        return a
    else:
        for j in range(2):
            b = min(b, ab_prune(d+1, i*2+j, True, v, a, b, md))
            if b <= a: break
        return b

n = int(input("Enter number of leaf nodes (power of 2): "))
v = list(map(int, input(f"Enter {n} leaf node values: ").split()))
print("Optimal value:", ab_prune(0, 0, True, v, -math.inf, math.inf, int(math.log2(n))))