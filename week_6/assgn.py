import random

reads = list()
min_len = 1000000000
for i in range(97):
  read_name = input()
  read_data = input()
  reads.append([read_name, read_data])
  min_len = min(min_len, len(read_data))

k = 10
motifs = list()
for read in reads:
  # motifs.append(read[1][0:k])
  start_pos = random.randint(0, len(read[1]) - k)
  motifs.append(read[1][start_pos:start_pos+k])
# ccataaatat
for e in range(100):
  profile = {
    'a': [1] * k,
    't': [1] * k,
    'c': [1] * k,
    'g': [1] * k
  }
  for motif in motifs:
    for idex, j in enumerate(motif):
      profile[j][idex] += 1
  for c in "atcg":
    for i in range(k):
      profile[c][i] /= 101
  new_motifs = list()
  for read in reads:
    cur_max = ""
    max_score = -1
    for i in range(0, len(read) - k):
      score = 1
      for j in range(k):
        score *= profile[read[1][i+j]][j]
      if score > max_score:
          max_score = score
          cur_max = read[1][i:i+k]
    new_motifs.append(cur_max)
  motif = new_motifs
  if e % 100 == 0:
    print(f"{e} done")

print(motifs)
print(*[i for i in motifs], sep="\n")

answer = ""
for i in range(k):
  cur_max = 0
  cur_answer = 'X'
  for c in "atcg":
    if profile[c][i] > cur_max:
      cur_max = profile[c][i]
      cur_answer = c
  answer += cur_answer
print(answer)
    

# for i in range(0, min_len - k):
#   # randomized motif search
#   score = list()
#   for j in range(i, i+k):
#     score.append({
#       'a': 1,
#       't': 1,
#       'c': 1,
#       'g': 1
#     })
#     for l in range(97): 
#       score[-1][reads[l][1][j]] += 1
#     for c in "atcg":
#       score[-1][c] /= 101
#     for read in reads:
#       for l in range(0, len(read) - k):
#         s = 1
#         for m in range(l, l + k):
#           s *= score[m - l][read[m]]
#       if s > max_s:
#         max_s = s


#   print(score)
      