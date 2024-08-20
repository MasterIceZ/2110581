lines = list()
while True:
    try:
        lines.append(input())
    except EOFError:
        break

adj = dict()
degIn = dict()
degOut = dict()

idx = 0
for line in lines:
    tokens = line.split(" -> ")
    u = tokens[0]
    adj[u] = list()
    degOut[u] = 0
    for v in tokens[1].split(","):
        idx += 1
        adj[u].append([v, idx])
        degOut[u] += 1
        if v not in degIn:
            degIn[v] = 0
        degIn[v] += 1

for k in degIn.keys():
    if k not in degOut:
        degOut[k] = 0
    if k not in adj:
        adj[k] = list()

for k in degOut.keys():
    if k not in degIn:
        degIn[k] = 0
    if k not in adj:
        adj[k] = list()

done = set()
path = list()
def dfs(u):
    if u not in adj.keys():
        return 
    for e in adj[u]:
        if e[1] in done:
            continue
        done.add(e[1])
        dfs(e[0])
    path.append(u)

stp = -1
for u in adj.keys():
    if degOut[u] - degIn[u] == 1:
        stp = u
dfs(stp)

print("->".join(path[::-1]))
