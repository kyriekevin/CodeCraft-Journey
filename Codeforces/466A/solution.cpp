/*
Platform: Codeforces
Problem: 466A - Cheap Travel
Rating: 1200
URL: https://codeforces.com/problemset/problem/466/A
Tags: implementation

Date: 2025-03-09
Time: 12:51

Author: Kyire
*/

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    int n, m, a, b;
    cin >> n >> m >> a >> b;
    if (a * m <= b) cout << a * n << endl;
    else cout << n / m * b + min((n % m) * a, b) << endl;

    return 0;
}
