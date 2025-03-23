/*
Platform: AcWing
Problem: 785 - 快速排序
Difficulty: Easy
URL: https://www.acwing.com/problem/content/787/

Date: 2025-03-22
Time: 15:56

Author: Kyire
*/


#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e5 + 10;
int g[N];
int n;

void quick_sort(int left, int right) {
    if (left >= right) return;

    int x = g[left + right >> 1], l = left - 1, r = right + 1;

    while (l < r) {
        while (g[++l] < x);
        while (g[--r] > x);
        if (l < r) swap(g[l], g[r]);
    }

    quick_sort(left, r);
    quick_sort(r + 1, right);
}
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> g[i];
    quick_sort(0, n - 1);
    for (int i = 0; i < n; i++) cout << g[i] << " ";

    return 0;
}
