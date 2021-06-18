class Solution:
    def sortSentence(self, s: str) -> str:
        arr = []
        new_s = s.split(" ")
        for x in new_s:
            arr.append((int(x[-1]), x[:-1])) 
        arr.sort()
        return " ".join(arr[i][1] for i in range(len(arr)))
            