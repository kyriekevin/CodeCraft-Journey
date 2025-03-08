/*
Platform: AcWing
Problem: 6122 - 农夫约翰的奶酪块
Difficulty: Easy
URL: https://www.acwing.com/problem/content/6125/

Date: 2025-03-08
Time: 11:05

Author: Kyire
*/

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1010;
int a[N][N], b[N][N], c[N][N];
int n;

int main() {
    int q;
    cin >> n >> q;

    int res = 0;
    for (int i = 0; i < q; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        if (++a[x][y] == n) res++;
        if (++b[y][z] == n) res++;
        if (++c[x][z] == n) res++;
        cout << res << endl;
    }

    return 0;
}
