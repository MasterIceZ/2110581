#include <bits/stdc++.h>

using namespace std;
using pii = pair<int, int>;
using ppi = pair<pii, int>;

const int MATCH_SCORE = 3;
const int SUB_PENALTY = -3;
const int GAP_PENALTY = -2;

struct fenwick_tree {
  vector<vector<int>> t;
  int n, m;
  fenwick_tree(int _n, int _m):
    n(_n), m(_m) {
      t = vector<vector<int>> (n + 1, vector<int> (m + 1));
  }
  void update(int idx_i, int idx_j, int v) {
    for(int i=idx_i; i<=n; i+=i&-i) {
      for(int j=idx_j; j<=m; j+=j&-j) {
        t[i][j] = max(t[i][j], v);
      }
    }
  }
  int query(int idx_i, int idx_j) {
    int res = 0;
    for(int i=idx_i; i>0; i-=i&-i) {
      for(int j=idx_j; j>0; j-=j&-j) {
        res = max(res, dp[i][j])
      }
    }
  }
}

inline int s(char a, char b) {
	return a == b ? MATCH_SCORE: SUB_PENALTY;
}

inline int W(int n) {
	return n * GAP_PENALTY;
}

signed main(int argc, char *argv[]) {
  string a = "ACGCGCAGC", b = "GCGCGCGCG";
  int n = a.size(), m = b.size();
	a = " " + a, b = " " + b;
	vector<vector<int>> dp(n + 1, vector<int> (m + 1, 0));
	vector<vector<ppi>> backtrack(n + 1, vector<ppi> (m + 1));
	for(int i=1; i<=n; ++i) {
		for(int j=1; j<=m; ++j) {
			dp[i][j] = max({
				0,
				dp[i - 1][j - 1] + s(a[i], b[j]), 
				dp[i - 1][j] + W(1), 
				dp[i][j - 1] + W(1)
			});
			if(dp[i][j] == dp[i - 1][j - 1] + s(a[i], b[j])) {
				backtrack[i][j] = make_pair(make_pair(i - 1, j - 1), 1);
			}
			else if(dp[i][j] == dp[i - 1][j] + W(1)) {
				backtrack[i][j] = make_pair(make_pair(i - 1, j), 2);
			}
			else if(dp[i][j] == dp[i][j - 1] + W(1)) {
				backtrack[i][j] = make_pair(make_pair(i, j - 1), 3);
			}
			else {
				backtrack[i][j] = make_pair(make_pair(i, j), 4);
			}
		}
	}
	pii start_backtrack = make_pair(-1, -1);
	int cur_max = 0;
	for(int j=1; j<=m; ++j) {
		for(int i=1; i<=n; ++i) {
			cout << dp[i][j] << " ";
			if(dp[i][j] > cur_max) {
				cur_max = dp[i][j];
				start_backtrack = make_pair(i, j);
			}
		}
		cout << "\n";
	}
	pii cur = start_backtrack;
	string answer_1 = "", answer_2 = "";
	while(backtrack[cur.first][cur.second].second != 4) {
		switch(backtrack[cur.first][cur.second].second) {
			case 1:
				answer_1 += a[cur.first];
				answer_2 += b[cur.second];
				break;
			case 2:
				answer_1 += a[cur.first];
				answer_2 += "-";
				break;
			case 3:
				answer_1 += "-";
				answer_2 += b[cur.second];
				break;
		}
		cur = backtrack[cur.first][cur.second].first;
	}
	reverse(answer_1.begin(), answer_1.end());
	reverse(answer_2.begin(), answer_2.end());
	cout << answer_1 << "\n" << answer_2 << "\n";
	return 0;
}
