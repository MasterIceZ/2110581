import numpy as np
from math import sqrt
import sys

def read_data(f, t):
  for l in f:
    yield list(map(t, l.split()))

def distance(a, b):
  return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def assign_centroids(p, centroids):
  dists = [distance(p, c) for c in centroids]
  return dists.index(min(dists))

def get_centroid(pts, assign, iteration):
  d = [p for p, a in zip(pts, assign) if a == iteration]
  return np.mean(np.array(d), axis=0)

def k_means(pts, k, iteration=30):
  centroids = pts[:k]
  for _ in range(iteration):
    assign = [assign_centroids(p, centroids) for p in pts]
    centroids = [get_centroid(pts, assign, i) for i in range(k)]
  return centroids

f = open(sys.argv[1])

k, m = next(read_data(f, int))
pts = [np.array(pts) for pts in read_data(f, float)]
for m in k_means(pts, k):
  print(*[f"{x:.3f}" for x in m])
