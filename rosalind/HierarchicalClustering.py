import numpy as np
from collections import defaultdict
import sys

def closest(d):
  d = np.copy(d)
  np.fill_diagonal(d, d.max() + 1)
  return divmod(d.argmin(), d.shape[1])

def avg_indx(d, i, j, di, dj):
  d = np.copy(d)
  avg = (d[i, :] * di + d[j, :] * dj) / (di + dj)
  d[i, :] = avg
  d[:, i] = avg
  d = np.delete(d, j, 0)
  d = np.delete(d, j, 1)
  np.fill_diagonal(d, 0)
  return d

def get_descendant_list(t, stp):
  q = [stp]
  res = list()
  while len(q):
    cur = q.pop(0)
    if cur in t:
      q.append(t[cur])
    else:
      res.append(cur)
  return res

def create_cluster(d, n):
  clusters = list(range(1, n + 1))
  t = dict()
  sz = defaultdict(lambda: 1) 
  cur = n
  while len(clusters) > 1:
    cur += 1
    i, j = closest(d)
    a, b = clusters[i], clusters[j]
    t[cur] = [a, b]
    sz[cur] = sz[a] + sz[b]
    d = avg_indx(d, *closest(d), sz[a], sz[b])
    clusters[i] = cur
    del clusters[j]
    yield get_descendant_list(t, a) + get_descendant_list(t, b)

n, *m = open(sys.argv[1]).read().splitlines()
m = np.array([list(map(float, x.split())) for x in m])

for st in create_cluster(m, int(n)):
  print(*st)