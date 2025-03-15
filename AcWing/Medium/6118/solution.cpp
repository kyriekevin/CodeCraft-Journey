/*
Platform: AcWing
Problem: 6118 - 蛋糕游戏
Difficulty: Medium
URL: https://www.acwing.com/problem/content/6121/

Date: 2025-03-15
Time: 19:21

Author: Kyire
*/

#include <climits>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long ll;
const int N = 5e5 + 10;
ll g[N];
int n, m;

int main() {
    cin >> m;
    while (m--) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> g[i];
            g[i] += g[i - 1];
        }

        ll res = LLONG_MAX;
        for (int l = 1; 2 * l <= n; l++) {
            res = min(res, g[l + n / 2] - g[l - 1]);
        }
        cout << res << " " << g[n] - res << endl;
    }
    return 0;
}
