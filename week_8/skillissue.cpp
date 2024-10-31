#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const string WANT = "THHTTHTT";
// const string WANT = "TTTTTTTHHHHHHH";

unordered_map<char, double> prob_state[2];

map<double, set<vector<bool>>> pbs;
double all_prob = 0;

void brute(int n, double prob, vector<bool> states) {
  if(n == (int) WANT.size()) {
    prob += prob_state[states[n - 1]][WANT[n - 1]];
    for(int i=1; i<(int) states.size(); ++i) {
      prob += (states[i] != states[i - 1] ? log(0.1): log(0.9));
    }
    all_prob += exp(prob);
    pbs[prob].emplace(states);
    return ;
  }
  states.emplace_back(false);
  brute(n + 1, prob + prob_state[0][WANT[n]], states);
  states.pop_back();
  states.emplace_back(true);
  brute(n + 1, prob + prob_state[1][WANT[n]], states);
}

signed main(int argc, char *argv[]) {
  cin.tie(nullptr)->ios::sync_with_stdio(false);
  prob_state[0]['H'] = log(0.5);
  prob_state[0]['T'] = log(0.5);
  prob_state[1]['H'] = log(0.75);
  prob_state[1]['T'] = log(0.25);
  // brute(0, 0, {});
  brute(1, log(0.5), {0});
  brute(1, log(0.5), {1});
  auto it = pbs.rbegin();
  cout << "PROB: " << exp(it->first) << "\n";
  for(auto v: it->second) {
    for(auto x: v) {
      cout << (x ? "B": "F");
    }
    cout << "\n";
  }
  cout << "ALL PROB:" << fixed << setprecision(6) << all_prob << "\n";
  return 0;
}