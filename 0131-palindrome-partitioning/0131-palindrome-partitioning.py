class Solution:
    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def helper(self, index, s, path, palindrome):
        #print("index = {} , Path so Far = {} palindrom = {}".format(index,path,palindrome))
        if index == len(s):
            #print("In end Adding path to Palindrome")
            palindrome.append(path[:])
            return
        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                path.append(s[index:i+1])
                self.helper(i+1, s, path, palindrome)
                path.pop()
    
    def partition(self, s: str) -> List[List[str]]:
        palindrome = []
        path = []
        self.helper(0, s, path, palindrome)
        return palindrome

    

    