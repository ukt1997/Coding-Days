class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        if n <= 1:
            return ''
        else:
            for i in range(n):
                if palindrome[i] != 'a' and i != n//2:
                    return palindrome[:i] + 'a' + palindrome[i+1:]
            return palindrome[:-1] + 'b'
        return palindrome
        