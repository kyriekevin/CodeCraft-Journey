#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

const int N = 1e4 + 10, M = 2e5 + 10, K = 110;
int n, m, k, s;
int h[N], e[M], ne[M], idx;
int q[N], dist[N][K], id[N];

void add(int a, int b) { e[idx] = b, ne[idx] = h[a], h[a] = idx++; }

void bfs(int p) {
  int hh = 0, tt = -1;
  for (int i = 1; i <= n; i++) {
    if (id[i] == p) {
      dist[i][p] = 0;
      q[++tt] = i;
    }
  }

  while (hh <= tt) {
    int t = q[hh++];
    for (int i = h[t]; ~i; i = ne[i]) {
      int j = e[i];
      if (dist[j][p] == -1) {
        dist[j][p] = dist[t][p] + 1;
        q[++tt] = j;
      }
    }
  }
}

int main() {
  while (~scanf("%d%d%d%d", &n, &m, &k, &s)) {
    for (int i = 1; i <= n; i++)
      scanf("%d", &id[i]);

    memset(h, -1, sizeof h);
    memset(dist, -1, sizeof dist);
    idx = 0;

    while (m--) {
      int a, b;
      scanf("%d%d", &a, &b);
      add(a, b), add(b, a);
    }

    for (int i = 1; i <= k; i++)
      bfs(i);
    for (int i = 1; i <= n; i++) {
      sort(dist[i] + 1, dist[i] + k + 1);
      int res = 0;
      for (int j = 1; j <= s; j++)
        res += dist[i][j];
      printf("%d ", res);
    }
    puts("");
  }

  return 0;
}
