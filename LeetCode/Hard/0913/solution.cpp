/*
Platform: LeetCode
Problem: 913 - Cat and Mouse
Difficulty: Hard
URL: https://www.leetcode.com/problems/cat-and-mouse/

Date: 2025-02-10
Time: 23:45

Author: Kyire

Algorithm: Topological Sort
Time Complexity: O(n^3)
Space Complexity: O(n^2)

Runtime: 107 ms
Memory: 48.1 MB
*/

const int N = 55;

class Solution {
private:
    int f[N][N][2], deg[N][N][2];
public:
    int catMouseGame(vector<vector<int>> &graph) {
        int n = graph.size();
        memset(f, 0, sizeof f);

        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n; j++) {
                deg[i][j][0] = graph[i].size();
                deg[i][j][1] = graph[j].size();
            }

            for (int j: graph[0])
                 deg[i][j][1]--;
        }

        queue<tuple<int, int, int>> q;
        for (int i = 1; i < n; i++) {
            f[0][i][1] = 1;
            f[i][i][0] = f[i][i][1] = 2;
            q.emplace(0, i, 1);
            q.emplace(i, i, 0);
            q.emplace(i, i, 1);
        }

        auto get_pre_states = [&](int mouse, int cat, int turn) {
            vector<pair<int, int>> pre_states;
            if (turn == 0) {
                for (int pre_cat: graph[cat])
                    if (pre_cat != 0 && f[mouse][pre_cat][1] == 0)
                        pre_states.emplace_back(mouse, pre_cat);
            }
            else {
                for (int pre_mouse: graph[mouse])
                    if (f[pre_mouse][cat][0] == 0)
                        pre_states.emplace_back(pre_mouse, cat);
            }
            return pre_states;
        };

        while (q.size()) {
            auto [mouse, cat, turn] = q.front();
            q.pop();
            int win = f[mouse][cat][turn];
            int pre_turn = turn ^ 1;
            for (auto [pre_mouse, pre_cat]: get_pre_states(mouse, cat, turn)) {
                if (pre_turn == win - 1 || --deg[pre_mouse][pre_cat][pre_turn] == 0) {
                    f[pre_mouse][pre_cat][pre_turn] = win;
                    q.emplace(pre_mouse, pre_cat, pre_turn);
                }
            }
        }

        return f[1][2][0];
    }
};
