class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = [i for i in nums]
        print(ret)
        for i in nums:
            ret.append(i)
        return ret
        