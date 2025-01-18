# include <iostream>
using namespace std;

int main() {
  int n, t, res = 0;
  cin >> n >> t;
  while (n--) {
    int x;
    cin >> x;
    if (t >= x) {
      res ++;
      t -= x;
    }
    else break;
  }
  cout << res << endl;

  return 0;
}
