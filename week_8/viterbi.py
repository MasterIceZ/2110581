from operator import itemgetter
from collections import deque

def parse_matrix(lines):
  res = dict()
  _, *other = [line.split() for line in lines]
  for line in other:
    state, *values = line
    for i, value in enumerate(values):
      res[state, value] = float(values[i])
  return res

def viterbi(x, transitions, emissions, backtrack):
  states = {si for si, _ in transitions}
  m = {(0, s): emissions[s, x[0]] * backtrack[s] for s in states}
  trace = {(0, s): None for s in states}

  for i, c in enumerate(x):
    for s in states:
      if i == 0:
        continue
      p, o = max([(m[i - 1, si] * transitions[si, s], si) for si in states], key=itemgetter(0))
      m[i, s] = emissions[s, c] * p
      trace[i, s] = o
  return m, trace

def do_backtrack(t, pos):
  i, s, st = *pos, deque()
  while i>=0:
    st.appendleft(s)
    s = t[i, s]
    i -= 1
  return ''.join(st)

lines = list()
with open('sample.in', 'r') as f:
  for line in f:
    if not line.startswith('-'):
      lines.append(line)

x = lines[0]
alpha = lines[1].split()
states = lines[2].split()

transitions = parse_matrix(lines[3:3 + len(states) + 1])
emissions = parse_matrix(lines[3 + len(states) + 1:3 + len(states) * 2 + 2])

backtrack = {s: 1 / len(states) for s in states}
matrix, trace = viterbi(x, transitions, emissions, backtrack)
_, ending = max([(matrix[len(x) - 1, s], s) for s in states])
print(do_backtrack(trace, (len(x) - 1, ending)))