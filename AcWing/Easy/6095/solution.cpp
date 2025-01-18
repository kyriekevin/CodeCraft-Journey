/*
Platform: AcWing
Problem: 6098 - 参加比赛
Difficulty: Easy
URL: https://www.acwing.com/problem/content/6098/

Date: 2025-01-18
Time: 23:05

Author: Kyire
*/

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
