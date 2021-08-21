class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 
            r += 1
        return s[l+1:r]
    
    # self.helper(s,i,i) 處理 odd case，每個字母自己都是 palindrome，左邊-1，右邊+1，去看這個字母的兩邊是否相等
    # self.helper(s,i,i+1) 處理 even case，先判斷相鄰兩個是不是相同，左邊-1，右邊+1，去看這兩個字母的兩邊是否相等
