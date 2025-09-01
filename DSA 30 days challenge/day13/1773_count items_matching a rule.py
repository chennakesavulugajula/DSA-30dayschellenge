class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic={"type":0,"color":1,"name":2}
        id=dic[ruleKey]
        count=0
        for i in items:
            if i[id]==ruleValue:
                count+=1
        return count
