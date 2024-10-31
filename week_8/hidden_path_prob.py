import numpy as np
import pandas as pd

with open("1.txt", "r") as f:
  want = f.readline().strip()
  _ = f.readline()
  states = f.readline().strip().split()
  f.readline()
  transition_prob = pd.DataFrame(np.full((len(states), len(states)), 0), index=states, columns=states)
  states_col = f.readline().strip().split()
  for line in f:
    l = line.strip().split()
    for i in range(1, len(l)):
      transition_prob.loc[l[0], states_col[i-1]] = float(l[i])
  
  answer = 0.5
  for j in range(len(want) - 1):
    answer *= transition_prob.loc[want[j], want[j + 1]]
  
  print(answer)