ref_file = open('spade.fastq', 'r')
ref = ref_file.readlines()[1]

reads1_file = open('reads1.fastq', 'r')
reads1 = [read[:-1] for read in reads1_file.readlines()[1::2]]

reads2_file = open('reads2.fastq', 'r')
reads2 = [read[:-1] for read in reads2_file.readlines()[1::2]]

print(len(reads1), len(reads2))

reads1_zip = sorted(zip([ref.find(read) for read in reads1], reads1))
reads2_zip = sorted(zip([ref.find(read) for read in reads2], reads2))

answer = [" " * len(ref)] * len(reads1)

c = 0
for idnt, read in reads1_zip:
  if idnt == -1:
    continue
  answer[c] = answer[c][:idnt] + read + ">1" + answer[c][idnt + 14:]
  c += 1

c = 0
for idnt, read in reads2_zip:
  if idnt == -1:
    continue
  answer[c] = answer[c][:idnt] + read + f">2" + answer[c][idnt + 14:]
  c += 1

# print(answer)

with open('act_2_3.txt', 'w') as f:
  f.write(ref)
  for read in answer:
    f.write(read + "\n")
