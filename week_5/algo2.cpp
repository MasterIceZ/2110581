#include <bits/stdc++.h>

using namespace std;
using pii = pair<int, int>;
using ppi = pair<pii, int>;

const string PAM250_CHRS = "ACDEFGHIKLMNPQRSTVWY";
const int MATCH_SCORE = 3;
const int SUB_PENALTY = -3;
const int GAP_PENALTY = -5;

const vector<vector<int>> PAM250 = {
    { 2, -2,  0,  0, -3,  1, -1, -1, -1, -2, -1,  0,  1,  0, -2,  1,  1,  0, -6, -3 },
    {-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4,  0, -2, -2, -8,  0 },
    { 0, -5,  4,  3, -6,  1,  1, -2,  0, -4, -3,  2, -1,  2, -1,  0,  0, -2, -7, -4 },
    { 0, -5,  3,  4, -5,  0,  1, -2,  0, -3, -2,  1, -1,  2, -1,  0,  0, -2, -7, -4 },
    {-3, -4, -6, -5,  9, -5, -2,  1, -5,  2,  0, -3, -5, -5, -4, -3, -3, -1,  0,  7 },
    { 1, -3,  1,  0, -5,  5, -2, -3, -2, -4, -3,  0,  0, -1, -3,  1,  0, -1, -7, -5 },
    {-1, -3, -2, -2,  1, -2,  6, -2,  0, -2, -2,  2,  0,  3,  2, -1, -1, -2, -3,  0 },
    {-1, -2, -2, -2,  1, -3, -2,  5, -2,  2,  2, -2, -2, -2, -2, -1,  0,  4, -5, -1 },
    {-1, -5,  0,  0, -5, -2,  0, -2,  5, -3,  0,  1, -1,  1,  3,  0,  0, -2, -3, -4 },
    {-2, -6, -4, -3,  2, -4, -2,  2, -3,  6,  4, -3, -3, -2, -3, -3, -2,  2, -2, -1 },
    {-1, -5, -3, -2,  0, -3, -2,  2,  0,  4,  6, -2, -2, -1,  0, -2, -1,  2, -4, -2 },
    { 0, -4,  2,  1, -3,  0,  2, -2,  1, -3, -2,  0,  6,  0,  0,  1,  0, -1, -6, -5 },
    { 1, -5, -1, -1, -5,  0,  0, -2, -1, -3, -2,  0,  0,  6,  0,  1,  0, -1, -6, -5 },
    { 0, -5, -3,  2, -5, -3, -1, -2,  1, -2, -1,  1,  0,  0,  4, -1, -1, -2, -5, -4 },
    {-2, -4, -3, -1, -4, -3, -3, -2,  3, -3,  0, -2, -3,  1, -1,  0, -2, -1,  2, -4 },
    { 1,  0,  0,  0, -3,  1, -1, -1,  0, -3, -2,  1,  1, -1,  0,  2,  1, -1, -2, -3 },
    { 1, -2,  0,  0, -3,  0, -1,  0,  0, -2, -1,  0,  0, -1,  2,  3,  0,  4, -6, -2 },
    { 0, -2, -2, -2, -1, -1, -2,  4, -2,  2,  2, -2, -1, -2, -2, -1,  0,  4, -6, -2 },
    {-6, -8, -7, -7,  0, -7, -3, -5, -3, -2, -4, -4, -6, -5,  2, -2, -5, -6, 17,  0 },
    {-3,  0, -4, -4,  7, -5,  0, -1, -4, -1, -2, -2, -5, -4,  0, -3, -3,  0,  0, 10 }
};

inline int get_index(char x) {
	int res = -1;
	for(int i=0; i<(int) PAM250_CHRS.size(); ++i) {
		if(x == PAM250_CHRS[i]) {
			res = i;
		}
	}
	assert(res != -1);
	return res;
}

inline int s(char a, char b) {
	// return a == b ? MATCH_SCORE: SUB_PENALTY;
	return PAM250[get_index(a)][get_index(b)];
}

inline int W(int n) {
	return n * GAP_PENALTY;
}

signed main(int argc, char *argv[]) {
	string a, b;
	cin >> a >> b;
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
//			cout << dp[i][j] << " ";
			if(dp[i][j] > cur_max) {
				cur_max = dp[i][j];
				start_backtrack = make_pair(i, j);
			}
		}
//		cout << "\n";
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
	cout << cur_max << "\n";
	cout << answer_1 << "\n" << answer_2 << "\n";
	return 0;
}