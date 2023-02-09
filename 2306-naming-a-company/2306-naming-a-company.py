class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        dic={}
        visited=set()
        count=0

        for idea in ideas:
            if idea[0] not in dic:
                dic[idea[0]]=set()
            dic[idea[0]].add(idea[1:])

        for key1,set1 in dic.items():
            visited.add(key1)
            for key2,set2 in dic.items():
                if key2 in visited:
                    continue
                overlap=len(set1.intersection(set2))
                count+=((len(set1)-overlap)*(len(set2)-overlap)*2)

        return count
        