/*
Platform: AcWing
Problem: 6135 - 奶牛体检
Difficulty: Easy
URL: https://www.acwing.com/problem/content/6138/

Date: 2025-03-16
Time: 11:08

Author: Kyire
*/

#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 7510;
int a[N], b[N], res[N];
int n, cnt;

int main() {
  cin >> n;
  for (int i = 1; i <= n; i++)
    cin >> a[i];
  for (int i = 1; i <= n; i++)
    cin >> b[i];

  for (int i = 1; i <= n; i++)
    if (a[i] == b[i])
      cnt++;

  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < 2; j++) {
      int cur = cnt;
      for (int l = i, r = i + j; l >= 1 && r <= n; l--, r++) {
        if (a[l] == b[l])
          cur--;
        if (a[r] == b[r])
          cur--;
        if (a[l] == b[r])
          cur++;
        if (a[r] == b[l])
          cur++;
        res[cur]++;
      }
    }
  }

  for (int i = 0; i <= n; i++)
    cout << res[i] << endl;

  return 0;
}
