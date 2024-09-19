#include <bits/stdc++.h>

using namespace std;

signed main(int argc, char *argv[]) {
	cin.tie(nullptr)->ios::sync_with_stdio(false);
	string s, t;
	cin >> s >> t;
	int n = (int) s.size(), m = (int) t.size();
	s = " " + s; t = " " + t;
	vector<vector<int>> dp(n + 1, vector<int> (m + 1));
	for(int i=1; i<=n; ++i) {
		dp[i][0] = i;
	}
	for(int i=1; i<=m; ++i) {
		dp[0][i] = i;
	}
	for(int i=1; i<=n; ++i) {
		for(int j=1; j<=m; ++j) {
			if(s[i] == t[j]) {
				dp[i][j] = dp[i - 1][j - 1];
			}
			else {
				dp[i][j] = min({dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]}) + 1;
			}
		}
	}
	cout << dp[n][m] << "\n";
	return 0;
}
