class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        on_hand_5 = 0
        on_hand_10 = 0
        for num in bills:
            if num == 5:
                on_hand_5 += 1
            elif num == 10 :
                on_hand_5 -= 1
                if on_hand_5 < 0:
                    return False
                on_hand_10 += 1
            else:
                if on_hand_10:
                    on_hand_5 -= 1
                    on_hand_10 -= 1
                else:
                    on_hand_5 -= 3
                if on_hand_5 < 0 or on_hand_10 < 0:
                    return False
        return True
        