/*
Platform: AcWing
Problem: 6099 - 座位
Difficulty: Medium
URL: https://www.acwing.com/problem/content/6102/

Date: 2025-02-15
Time: 17:21

Author: Kyire
*/

#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

const int N = 1e5 + 10;
vector<int> q[N];
int path[4], res[N];
bool st[4], used[N];
int n;

int get(int x, int a, int b, int c) {
    for (int v: q[x]) {
        if (v != a && v != b && v != c)
            return v;
    }
    return -1;
}

bool check() {
    res[2] = 1;
    int d[] = {0, 1, 3, 4};
    for (int i = 0; i < 4; i++)
        res[d[i]] = q[1][path[i]];

    for (int i = 5; i < n + 5; i++) {
        res[i] = get(res[i - 2], res[i - 4], res[i - 3], res[i - 1]);
        if (res[i] == -1) return false;
    }

    for (int i = 0; i < 5; i++)
        if (res[i] != res[n + i])
            return false;

    memset(used, 0, sizeof used);
    for (int i = 0; i < n; i++) {
        int x = res[i];
        if (used[x]) return false;
        used[x] = true;
    }

    for (int i = 0; i < n; i++)
        cout << res[i] << " ";

    return true;
}

bool dfs(int u) {
    if (u == 4) return check();

    for (int i = 0; i < 4; i++) {
        if (!st[i]) {
            path[u] = i;
            st[i] = true;
            if (dfs(u + 1)) return true;
            st[i] = false;
        }
    }

    return false;
}

int main() {
    cin >> n;
    for (int i = 0; i < 2 * n; i++) {
        int a, b;
        cin >> a >> b;
        q[a].push_back(b);
        q[b].push_back(a);
    }

    if (!dfs(0)) puts("-1");

    return 0;
}
