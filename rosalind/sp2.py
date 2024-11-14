N = int(input())
distance = list()
for i in range(N) :
  distance.append([float(x) for x in input().split()])
cluster = [str(i+1) for i in range(N)]
points_in_cluster = [[i] for i in range(N)]

def calc_distance(a: int, b: int) :
  ret = 0
  for i in points_in_cluster[a] :
    for j in points_in_cluster[b] :
      ret += distance[i][j]
  return ret / (len(points_in_cluster[a])*len(points_in_cluster[b]))

while len(cluster) > 1 :
  n = len(cluster)
  min_distance = 200000000
  best_pair = [0, 0]
  for i in range(n) :
    for j in range(n) :
      if (j <= i) : continue
      dis = calc_distance(i, j)
      if (dis < min_distance) :
        min_distance = dis
        best_pair = [i, j]
  
  a, b = best_pair
  new_cluster = cluster[a] + " " + cluster[b]
  for i in points_in_cluster[b] :
    points_in_cluster[a].append(i)
  cluster[a] = new_cluster
  print(new_cluster)
  cluster.pop(b)
  points_in_cluster.pop(b)