class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for st in strs:
                d["".join(sorted(st))].append(st)
            
        res = []
        for k in d.keys():
            res.append(list(d[k]))
        return res

            
        