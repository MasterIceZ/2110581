d1 = {
    "read_009": "GCAGCCCGTC",
    "read_011": "CCCGTCTTCA",
    "read_015": "TCTTCACGGT",
    "read_008": "CACGGTTGGA",
    "read_016": "GTTGGAAGGG",
    "read_010": "GAAGGGGGGG",
    "read_013": "GGGGGGCCCG",
    "read_007": "GGCCCGGCAC",
    "read_012": "CGGCACCGCG",
    "read_003": "ACCGCGCGCG",
    "read_002": "CGCGCGGGTG",
    "read_004": "CGGGTGATTC",
    "read_005": "TGATTCCTCC",
    "read_014": "TCCTCCGGGG",
    "read_001": "CCGGGGGCCC",
    "read_006": "GGGCCCCCGG"
}

d2 = {
    "read_009": "CCCGGCACCG",
    "read_011": "GCACCGCGCG",
    "read_015": "CGCGCGCGGG",
    "read_008": "CGCGGGTGAT",
    "read_016": "GGTGATTCCT",
    "read_010": "ATTCCTCCGG",
    "read_013": "CTCCGGGGGC",
    "read_007": "GGGGGCCCCC",
    "read_012": "GCCCCCGGGC",
    "read_003": "CCGGGCGCGG",
    "read_002": "GCGCGGGCGG",
    "read_004": "GGGCGGTGCG",
    "read_005": "GGTGCGCCAG",
    "read_014": "CGCCAGCCGG",
    "read_001": "AGCCGGACAG",
    "read_006": "GGACAGCGCG"
}

merged = d1["read_009"]

k = [x for x in d1.keys()]

print(*k)

for i in k[1:]:
  merged += d1[i][6:]

merged_back = ""

for i in k[10:-1:]:
  merged_back += d2[i][:4]
merged_back += d2[k[-1]]

print(merged)
print(merged_back)

print(len(merged), len(merged_back))

print(merged + merged_back)