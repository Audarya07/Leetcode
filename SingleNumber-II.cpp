class Solution {
public:
    int singleNumber(vector<int>& arr) {
        int n = arr.size();
        vector<int> cnt(32, 0);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < 32; j++){
                if(arr[i] & (1 << j)){
                    cnt[j]++;
                } 
            }
        }
        int res = 0;
        for(int i = 0; i < 32; i++){
            if(cnt[i] % 3 == 1){
                res += (1 << i);
            } 
        }
        return res;
    }
};