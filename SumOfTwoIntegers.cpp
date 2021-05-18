class Solution {
public:
    int getSum(int a, int b) {
        // a  --> holds running addition result
        // b  --> holds carries
        // ^  --> does actual addition
        // &  --> generates carries if any
        // << --> brings carry to required pos where it has to be applied 
        int c;
        while(b){
            c = a&b;
            a = a ^ b;
            b = (unsigned int)c << 1;
        }
        return a;
    }   
};