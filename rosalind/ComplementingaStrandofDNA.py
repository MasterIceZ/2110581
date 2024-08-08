parse_dict = {
  "A": "T",
  "T": "A",
  "C": "G",
  "G": "C"
}

print("".join(list(map(lambda x: parse_dict[x], input()[::-1]))))