/*
Platform: Luogu
Problem: P1923 - 【深基9.例4】求第 k 小的数
URL: https://www.luogu.com.cn/problem/P1923

Date: 2025-03-23
Time: 15:07

Author: Kyire
*/

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 5e6 + 10;
int g[N];

int quick_select(int s, int e, int k) {
    if (s >= e) return g[s];

    int x = g[s], l = s - 1, r = e + 1;
    while (l < r) {
        while (g[++l] < x);
        while (g[--r] > x);
        if (l < r) swap(g[l], g[r]);
    }

    if (r - s + 1 >= k)
        return quick_select(s, r, k);
    return quick_select(r + 1, e, k - (r - s + 1));
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> g[i];
    cout << quick_select(0, n - 1, k + 1) << endl;

    return 0;
}
