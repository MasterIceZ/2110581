s = "GCGGCCTAAGGCGCCCGCGC"
t = "GCGCGGGCGCCTTAGGCCGC"[::-1]

d = {
  'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'
}

t_parse = "".join([d[x] for x in t])

print(s)
print(t_parse)
print(s == t_parse)