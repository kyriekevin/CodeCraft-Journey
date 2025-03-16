/*
Platform: AcWing
Problem: 6123 - 哞叫时间
Difficulty: Easy
URL: https://www.acwing.com/problem/content/6126/

Date: 2025-03-15
Time: 14:38

Author: Kyire
*/


#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 2e4+10, M = 26;
char s[N];
int cnt[M][M];
bool st[M][M];
int n, m;

void update(int l, int r, int v) {
    l = max(l, 0), r = min(r, n - 1);
    for (int i = l; i + 2 <= r; i++) {
        char a = s[i], b = s[i + 1], c = s[i + 2];
        if (a != b && b == c) {
            cnt[a][b] += v;
            if (cnt[a][b] >= m)
                st[a][b] = true;
        }
    }
}
int main() {
    scanf("%d%d%s", &n, &m, s);
    for (int i = 0; i < n; i++)
        s[i] -= 'a';
    update(0, n - 1, 1);

    for (int i = 0; i < n; i++) {
        char t = s[i];
        update(i - 2, i + 2, -1);

        for (int j = 0; j < 26; j++) {
            if (j != t) {
                s[i] = j;
                update(i - 2, i + 2, 1);
                update(i - 2, i + 2, -1);
            }
        }
        s[i] = t;
        update(i - 2, i + 2, 1);
    }

    int res = 0;
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++)
            if (st[i][j])
                res++;

    }
    cout << res << endl;

    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++)
            if (st[i][j])
                printf("%c%c%c\n", i + 'a', j + 'a', j + 'a');
    }

    return 0;
}
