class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province = [0] * n
        print(province)
        cnt_province = 1
        stack = [0]
        province[0] = cnt_province
        while len(stack):
            cur = stack.pop(0)
            print(cur)
            for child, val in enumerate(isConnected[cur]):
                if val == 1 and province[child] == 0:
                    province[child] = province[cur]
                    stack.append(child)
            if len(stack) == 0:
                for i in range(n):
                    if province[i] == 0:
                        stack.append(i)
                        #print("Adding New Node", i)
                        cnt_province += 1
                        province[i] = cnt_province
                        
                        break
                    
                
        return cnt_province
        
        