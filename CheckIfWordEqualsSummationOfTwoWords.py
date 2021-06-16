class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        val_a = 0
        for i, x in enumerate(firstWord):
            val_a = val_a*10 + (ord(x)-97)
            
        val_b = 0
        for i, x in enumerate(secondWord):
            val_b = val_b*10 + (ord(x)-97)
            
        val_c = 0
        for i, x in enumerate(targetWord):
            val_c = val_c*10 + (ord(x)-97)
        
        if val_a + val_b == val_c:
            return True
        return False
       