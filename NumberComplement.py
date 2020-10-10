class Solution:
    def findComplement(self, num: int) -> int:
        #5 = 101   Now find the number 111 to mask with 101 , then subtract them for ans
        #14 = 1101 Now find the number 1111 to mask with 1101 , then subtract them for ans
        #Mask = pow(2, len(bin_num)) - 1  ...for num = 5
        #                |
        #              8(1000)       - 1 = 7(111)   
        
        bin_num = bin(num)[2:]
        return (2**len(bin_num) - 1) - num