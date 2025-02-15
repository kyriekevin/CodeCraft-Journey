/*
Platform: AcWing
Problem: 6100 - 奶牛选美
Difficulty: Hard
URL: https://www.acwing.com/problem/content/6103/

Date: 2025-02-15
Time: 16:58

Author: Kyire
*/

#include <iostream>
#include <cstring>
using namespace std;

const int N = 3e5 + 10;
int p[N], res[N];

int find(int x) {
    if (p[x] != x) p[x] = find(p[x]);
    return p[x];
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n + 1; i++) p[i] = i;

    while (m--) {
        int l, r, x;
        cin >> l >> r >> x;
        for (int i = l; i < x;) {
            i = find(i);
            if (i < x) {
                res[i] = x;
                p[i] = i + 1;
            }
        }

        for (int i = x + 1; i <= r;) {
            i = find(i);
            if (i <= r) {
                res[i] = x;
                p[i] = i + 1;
            }
        }
    }
    for (int i = 1; i <= n; i++)
        cout << res[i] << " ";

    return 0;
}
