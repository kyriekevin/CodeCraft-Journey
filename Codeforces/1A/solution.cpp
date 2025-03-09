/*
Platform: Codeforces
Problem: 1A - Theatre Square
Rating: 1000
URL: https://codeforces.com/contest/1/problem/A
Tags: math

Date: 2025-03-09
Time: 12:51

Author: Kyire
*/

#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long ll;

int main() {
    ll n, m, a;
    cin >> n >> m >> a;
    cout << (ll)ceil(n * 1.0 / a) * (ll)ceil(m * 1.0 / a) << endl;

    return 0;
}
