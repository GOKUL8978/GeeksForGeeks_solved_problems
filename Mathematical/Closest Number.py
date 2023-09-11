class Solution {
  public:
    int closestNumber(int N , int M) {
        return round(N/float(M))*M;
    }
};
