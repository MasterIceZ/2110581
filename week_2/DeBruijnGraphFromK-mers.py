lines = []

while True:
    try:
        lines.append(input())
    except EOFError:
        break

adj = dict()

for line in lines:
    u = line[:-1]
    v = line[1:]

    if u not in adj:
        adj[u] = list()
    adj[u].append(v)

list_keys = sorted(adj.keys())


for k in list_keys:
    adj[k].sort()
    print(f"{k} -> {",".join(adj[k])}")
