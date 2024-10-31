import numpy as np
import pandas as pd

with open("2.txt", "r") as f:
  x = f.readline().strip()
  _ = f.readline()
  t = f.readline().strip().split()
  _ = f.readline()
  want = f.readline().strip()
  _ = f.readline()
  states = f.readline().strip().split()
  _ = f.readline()
  emission = pd.DataFrame(np.full((len(states), len(t)), 0), index=states, columns=t)
  _ = f.readline()

  for line in f:
    l = line.strip().split()
    for i in range(1, len(l)):
      emission.loc[l[0], t[i-1]] = float(l[i])
  answer = 1
  for i in range(len(want)):
    answer *= emission.loc[want[i], x[i]]
  print(answer)