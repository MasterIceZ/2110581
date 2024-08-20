#include <bits/stdc++.h>

using namespace std;
using ll = long long;

vector<pair<string, string>> reads;
unordered_map<string, vector<pair<string, int>>> adj;
unordered_map<string, int> in, out;
set<string> kmers_set;
set<int> visited;
stack<string> res;
int cnt = 0;

void dfs(string u) {
  for(auto [v, id]: adj[u]) {
    if(visited.count(id)) {
      continue;
    }
    visited.emplace(id);
    dfs(v);
  }
  res.emplace(u);
}

signed main(int argc, char *argv[]) {
  string name, dna;
  while(cin >> name >> dna) {
    reads.emplace_back(name, dna);
  }
  int k = 3;
  for(auto [name, dna]: reads) {
    vector<string> kmers;
    for (int i = 0; i <= (int)dna.size() - k; ++i) {
      kmers.emplace_back(dna.substr(i, k));
    }
    for(auto kmer: kmers) {
      string pre = kmer.substr(0, k - 1);
      string suf = kmer.substr(1, k - 1);
      adj[pre].emplace_back(suf, ++cnt);
      in[pre]++, out[suf]++;
      kmers_set.emplace(pre);
      kmers_set.emplace(suf);
    }
  }
  string stp;
  for(auto kmer: kmers_set) {
    cerr << "D: " << kmer << " " << out[kmer] << " " << in[kmer] << "\n";
    if(out[kmer] - in[kmer] == 1) {
      stp = kmer;
      // break;
    }
  }
  dfs(stp);
  cerr << "SIZE: " << res.size() << "\n";
  while(!res.empty()) {
    cout << res.top() << "\n";
    res.pop();
  }
  return 0;
}