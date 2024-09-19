def get_profile(motifs, kmer) :
    n = len(motifs)
    profile = []
    for i in range(kmer) :
        cnt = {'A': 1, 'C': 1, 'T': 1, 'G': 1}
        for j in range(n) :
            cnt[motifs[j][i]] += 1
        profile.append(cnt)
    return profile
        
def get_motif(profile, dna, kmer) :
    motif = ""
    best_prob = -1
    m = len(dna)
    for j in range(m-kmer+1) :
      probability = 1
      for k in range(kmer) :
        probability *= (profile[k][dna[j+k]])/sum(profile[k].values())
      if (probability > best_prob) :
        best_prob = probability
        motif = dna[j:j+kmer]
    return motif

def score(profile) :
    score = 0
    for mp in profile :
       score += sum(mp.values()) - max(mp.values())
    return score

k, t = [int(i) for i in input().split()]
dna = list()
for i in range(t) :
    dna.append(input())

best_motifs = []
best_score = t * k
for i in range(len(dna[0]) - k) :
    motifs = [ dna[0][i:i+k] ]
    profile = get_profile(motifs, k)
    for j in range(1, t) :
      motifs.append(get_motif(profile, dna[j], k))
      profile = get_profile(motifs, k)
    s = score(profile)
    if (s < best_score) :
       best_score = s
       best_motifs = motifs

[print(i) for i in best_motifs]