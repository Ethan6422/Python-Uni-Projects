def A1(n):
    return 0.0045 * n**3

def A2(n):
    return 0.36 * n**2 + 0.15 * n


# Find the smallest n where A2 is faster than A1
n = 1
while A2(n) >= A1(n):
    n += 1

print(f"T2 becomes more time-efficient than T1 at n = {n}")
print(f"T1({n}) = {A1(n):.4f} seconds")
print(f"T2({n}) = {A2(n):.4f} seconds")
