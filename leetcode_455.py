class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookies = 0
        while child <= len(g)-1 and cookies <= len(s)-1:
            if g[child] <= s[cookies]:
                child+=1
                cookies+=1
            else:
                cookies+=1
        return child
