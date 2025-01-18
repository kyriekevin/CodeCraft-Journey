#include <iostream>
using namespace std;

typedef long long ll;

const int N = 1e5 + 10;
int s[N];
int n, t;

bool check(int x) {
  for (int i = 0; i + x <= n; i++) {
    ll tot = s[i + x] - s[i];
    if (tot <= t)
      return true;
  }
  return false;
}

int main() {
  cin >> n >> t;

  for (int i = 1; i <= n; i++) {
    int x;
    cin >> x;
    s[i] = s[i - 1] + x;
  }

  int l = 0, r = n;
  while (l < r) {
    int mid = l + r + 1 >> 1;
    if (check(mid)) l = mid;
    else r = mid - 1;
  }

  cout << l << endl;

  return 0;
}
