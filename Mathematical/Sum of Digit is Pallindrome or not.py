// User function Template for C++

class Solution {
  public:
    int isDigitSumPalindrome(int N) {
        int ans = 0;
        int pal = 0;
        int temp = N;
        while(N!= 0)
        {
            int digit = N%10;
            ans = ans + digit;
            N/=10;
        }
        int reverseans = ans;
        while(ans!= 0)
        {
            int rem = ans%10;
            pal = pal*10 + rem;
            ans/=10;
        }
        if(reverseans == pal)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
};
