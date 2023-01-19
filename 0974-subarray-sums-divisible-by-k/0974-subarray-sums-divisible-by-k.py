class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        div_sum = [0]*k
        div = 0
        total = 0
        for num in nums:
            print(num)
            div = (div + num) % k
            if div == 0:
                total += 1
            if div_sum[div]>0:
                total += div_sum[div]
                div_sum[div] += 1
            else:
                div_sum[div] = 1
            #print(div, div_sum , total)
        return total
        