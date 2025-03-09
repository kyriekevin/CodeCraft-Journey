/*
Platform: Codeforces
Problem: 4A - Watermelon
Rating: 800
URL: https://codeforces.com/problemset/problem/4/A
Tags: brute force, math

Date: 2025-03-08
Time: 13:44

Author: Kyire
*/

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    int x;
    cin >> x;
    if (x % 2 == 0 && x != 2) puts("YES");
    else puts("NO");

    return 0;
}
