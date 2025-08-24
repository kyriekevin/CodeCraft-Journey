class Solution {
public:
  int longestSubarray(vector<int> &nums) {
    int res = 0;
    for (int i = 0, j = 0, z = 0; i < nums.size(); i++) {
      if (nums[i] == 0)
        z++;
      while (z > 1)
        z -= !nums[j++];
      res = max(res, i - j);
    }
    return res;
  }
};
