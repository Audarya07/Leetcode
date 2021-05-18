// input =        [2,  3,  2,  2]
// binary_input = [10, 11, 10, 10]

// cnt =   [0,1,0,0,0,0,0,0,.....] --> 2
// cnt =   [1,2,0,0,0,0,0,0,.....] --> 3
// cnt =   [1,3,0,0,0,0,0,0,.....] --> 2
// cnt =   [1,4,0,0,0,0,0,0,.....] --> 2

// final_cnt =   [1%3=1,4%3=1,0,0,0,0,0,0,.....]
// final_cnt =   [(2**0)*1=1,(2**1)*1=2,0,0,0,0,0,0,.....]
// res = res+final_cnt[i];
// res = 1+2 = 3

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