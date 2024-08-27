s = input()

l = list(s)
l.sort()

while len(l[0]) < len(s):
    for i in range(len(s)):
        l[i] = s[i] + l[i]
    l.sort()
print(l[0][1:] + "$")
