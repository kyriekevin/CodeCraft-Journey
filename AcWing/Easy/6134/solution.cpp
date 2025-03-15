/*
Platform: AcWing
Problem: 6134 - 哞叫时间II
Difficulty: Easy
URL: https://www.acwing.com/problem/content/6137/

Date: 2025-03-15
Time: 22:08

Author: Kyire
*/

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long ll;

const int N = 1e6 + 10;
ll w[N], l[N], r[N];
int n;

int main() {
    cin >> n;

    ll res = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        w[i] = x;
        if (++l[x] == 1) cnt ++;
    }

    for (int i = n - 1; i > 0; i--) {
        int x = w[i];
        r[x]++, l[x]--;
        if (l[x] == 0) cnt--;
        if (r[x] == 2) {
            res += cnt;
            if (l[x] > 0) res--;
        }
    }

    cout << res << endl;

    return 0;
}
