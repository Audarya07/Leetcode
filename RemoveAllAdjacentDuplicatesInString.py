class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for x in s:
            if len(st) > 0 and x == st[-1]:
                st.pop()
            else:
                st.append(x)
        return "".join(st)