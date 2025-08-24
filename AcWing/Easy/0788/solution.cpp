#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

typedef long long LL;
const int N = 1e5 + 10;
int g[N], tmp[N];
int n;

LL msort(int l, int r) {
  if (l >= r)
    return 0;

  int mid = l + r >> 1;
  LL res = msort(l, mid) + msort(mid + 1, r);

  int i = l, j = mid + 1, k = 0;
  while (i <= mid && j <= r) {
    if (g[i] <= g[j])
      tmp[k++] = g[i++];
    else {
      res += mid - i + 1;
      tmp[k++] = g[j++];
    }
  }

  while (i <= mid)
    tmp[k++] = g[i++];
  while (j <= r)
    tmp[k++] = g[j++];

  for (int i = l; i <= r; i++)
    g[i] = tmp[i - l];

  return res;
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++)
    cin >> g[i];
  cout << msort(0, n - 1) << endl;

  return 0;
}
