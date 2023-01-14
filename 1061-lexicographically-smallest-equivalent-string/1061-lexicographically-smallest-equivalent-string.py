class Solution:
    
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def retindex(ch):
            return ord(ch) - ord('a')
        ret = ''
        chars = [chr(ord('a') + i) for i in range(26)]
        found = [-1] * 26
        mapping = []
        count_index = -1
        for index , ch in enumerate(s1):
            ch2 = s2[index]
            key = retindex(ch)
            value = retindex(ch2)
            i = found[key]
            j = found[value]
            #print(mapping)
            if i >= 0 and j >= 0:
                if i == j:
                    # already in same Group
                    continue
                else:
                    #print(i,j)
                    mapping[min(i,j)].extend(mapping[max(i,j)])
                    mapping.pop(max(i,j))
                    for temp in range(26):
                        if found[temp] == max(i,j):
                            found[temp] = min(i,j)
                        elif found[temp] >  max(i,j):
                            found[temp] -= 1
                    count_index -= 1
                    
            elif i >= 0:
                # Adding ch2 in same Group as ch
                mapping[i].append(ch2)
                found[value] = i
            elif j >= 0:
                # Adding ch in same Group as ch2
                mapping[j].append(ch)
                found[key] = j
            else:
                # Adding new Group 
                count_index += 1
                mapping.append([ch,ch2])
                found[key] = count_index
                found[value] = count_index
        #print(mapping)
        for grp in mapping:
            minch = min(grp)
            for ch in set(grp):
                if chars[retindex(ch)] > minch:
                    chars[retindex(ch)] = minch
        #print(chars)
        for ch in baseStr:
            ret += chars[retindex(ch)]
              
        return ret