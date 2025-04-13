typedef long long ll;
class Solution {
public:
  const int MOD = 1e9 + 7;

  ll qpow(ll x, ll n) {
    ll res = 1;
    while (n) {
      if (n & 1)
        res = res * x % MOD;
      x = x * x % MOD;
      n >>= 1;
    }

    return res;
  }

  int countGoodNumbers(long long n) {
    return qpow(5, (n + 1) / 2) * qpow(4, n / 2) % MOD;
  }
};
