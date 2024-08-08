#include <bits/stdc++.h>

using namespace std;
using ll = long long;

struct edge_t {
  string u, v, w;
  edge_t(string _u, string _v, string _w):
    u(_u), v(_v), w(_w) {}
};

vector<edge_t> edges;
vector<pair<string, string>> res;

signed main(int argc, char *argv[]) {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  string s, t;
  while(cin >> s >> t) {
    s.erase(0, 1);
    string u = t.substr(0, 3);
    string v = t.substr(t.size() - 3, 3);
    edges.emplace_back(u, v, s);
  }
  for(int i=0; i<(int) edges.size(); ++i) {
    for(int j=i+1; j<(int) edges.size(); ++j) {
      if(edges[i].v != edges[j].u) {
        continue;
      }
      res.emplace_back(edges[i].w, edges[j].w);
    }
  }
  for(auto [u, v]: res) {
    cout << u << " " << v << "\n";
  }
  return 0;
}