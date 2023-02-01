class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1
        if str1+str2 != str2+str1:
            return ""
        gcd_str = gcd(len(str1),len(str2))
        if str1[:gcd_str] == str2[:gcd_str]:
            return str1[:gcd_str]
        else:
            return ""
        