s = input()

l = list()
for i in range(len(s)):
    frnt = s[0]
    s = s[1:] + frnt
    l.append(s)
l.sort()

print("".join([x[-1] for x in l]))
