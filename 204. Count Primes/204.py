# Medium
# Topics: Array, Math, Enumeration, Number Theory

def countPrimes(n):
    if (n < 2): return 0

    is_prime = [True] * n   # [True, True, True, ..., True]
    is_prime[0] = is_prime[1] = False   #[False, False, True, ..., True]
    for i in range(2, n):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)        

# Input: 10
num = int(input())
print(countPrimes(num))     # 4