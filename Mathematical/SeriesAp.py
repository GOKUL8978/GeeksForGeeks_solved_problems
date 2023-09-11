//User function Template for C++
class Solution
{
public:
    vector<int> getTable(int N)
    {   
        vector<int> mul;
        int i=1;
        while(i<11){
            mul.push_back(N*i);
            i++;
        }
    return mul;
    }
};
