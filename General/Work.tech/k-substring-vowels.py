#https://workat.tech/problem-solving/practice/k-substring-vowels
class Solution:
	def kSubstringVowels(self, s: str, k: int) -> List[int]:
		# add your logic here
		out = []
		cnt = 0
		for i in range(0,k):
			if s[i] in 'aeiou':
				cnt += 1
		out.append(cnt)
		
		n = len(s)
		for i in range(k,n):
			if s[i-k] in 'aeiou':
				cnt -= 1
			if s[i] in 'aeiou':
				cnt += 1
			out.append(cnt)
		return out
		


