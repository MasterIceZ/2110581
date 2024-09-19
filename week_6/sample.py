# dp[i][j] = distance between a[0..i], b[0..j]
# dp[i][j] = dp[i - 1][j - 1] if a[i] == b[j] else min(dp[i - 1][j], dp[i][j - 1]) + 1

def levenshtein_distance(s, t):
    dp = [[1e9 + 100] * (len(t) + 1) for _ in range(len(s) + 1)]
    
    for i in range(len(s) + 1):
        dp[i][0] = i
    for j in range(len(t) + 1):
        dp[0][j] = j
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            dp[i][j] = dp[i - 1][j - 1] if s[i - 1] == t[j - 1] else (min(dp[i - 1][j], dp[i][j - 1]) + 1)
    
    return dp[len(s)][len(t)]

s = list()
for i in range(10):
  s.append(input())

for l in range(1, len(s[0])):
  for i in range(0, len(s[0]) - l):
    cur_s0 = s[0][i:i+l]
    found = 0
    for j in range(0, 10):
      for k in range(0, len(s[j]) - l):
        if levenshtein_distance(cur_s0, s[j][k:k+l]) <= 4:
          found += 1
    if found == 10:
      print(cur_s0, i, l)