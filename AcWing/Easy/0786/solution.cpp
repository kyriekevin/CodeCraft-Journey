/*
Platform: AcWing
Problem: 786 - 第k个数
Difficulty: Easy
URL: https://www.acwing.com/problem/content/788/

Date: 2025-03-23
Time: 14:56

Author: Kyire
*/

#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e5 + 10;
int g[N];

int quick_select(int start, int end, int k) {
  if (start >= end)
    return g[start];

  int x = g[start], l = start - 1, r = end + 1;
  while (l < r) {
    while (g[++l] < x)
      ;
    while (g[--r] > x)
      ;
    if (l < r)
      swap(g[l], g[r]);
  }

  if (r - start + 1 >= k)
    return quick_select(start, r, k);
  return quick_select(r + 1, end, k - (r - start + 1));
}

int main() {
  int n, k;
  cin >> n >> k;
  for (int i = 0; i < n; i++)
    cin >> g[i];
  cout << quick_select(0, n - 1, k) << endl;

  return 0;
}
