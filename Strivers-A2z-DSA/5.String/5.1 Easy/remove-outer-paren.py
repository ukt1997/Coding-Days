class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out = []
        stack = []
        cur_st = []
        for i in s:
            if i == '(':
                stack.append(i)
                cur_st.append('(')
            elif i == ')':
                if stack[len(stack) - 1] == '(':
                    cur_st.append(')')
                    stack.pop()
                    if len(stack) == 0:
                        out.append("".join(cur_st))
                        cur_st = []
                else:
                    stack.append(i)
                    cur_st.append(')')
            # print("Stack = ",stack)
            # print("out = ",out)
        ret = ""
        for i in out:
            n = len(i)
            ret += i[1:n - 1]
            # print(ret)
        return ret


