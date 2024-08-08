k, m, n = map(float, input().split())

p = n + m + k

AA = k / p
Aa = ((m / p) * (k / (p - 1))) + ((m / p) * ((m - 1) / (p - 1)) * 0.75) + ((m / p) * (n / (p - 1)) * 0.5)
aa = ((n / p) * (k / (p - 1))) + ((n / p) * (m / (p - 1)) * 0.5)

print(AA + Aa + aa)