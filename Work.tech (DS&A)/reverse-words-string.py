# https://workat.tech/problem-solving/practice/reverse-words-string

class Solution:
	def reverseWords(self, s: str) -> str:
		# add your logic here
		inp = s.split(" ")
		temp = reversed(inp)
		otp = ' '.join(temp)
		return otp
		 


