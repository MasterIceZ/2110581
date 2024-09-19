ref_file = open('reference.fastq', 'r')
ref = ref_file.readlines()[1]

reads1_file = open('reads1.fastq', 'r')
reads1 = [read[:-1] for read in reads1_file.readlines()[1::2]]

reads2_file = open('reads2.fastq', 'r')
reads2 = [read[:-1] for read in reads2_file.readlines()[1::2]]

read1_indices = list()
for idx, read in enumerate(reads1):
  try: 
    read1_indices.append((ref.index(read), idx + 1))
  except:
    read1_indices.append((-1, idx + 1))

read1_indices = sorted(read1_indices, key=lambda x: (x[0], x[1]))


print(read1_indices)
print()

with open('act_2.txt', 'w') as f:
  f.write(ref)
  for x in read1_indices:
    if x[0] == -1: 
      print(reads1[x[1] - 1])
      continue
    f.write(" " * x[0] + reads1[x[1] - 1] + " " * 20 + reads2[x[1] - 1] + "\n")