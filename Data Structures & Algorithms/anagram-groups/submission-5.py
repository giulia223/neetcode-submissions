class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for st in strs:
            s = "".join(sorted(st))
            if s in d.keys():
                d[s].append(st)
            else: d[s] = [st]
        l = []
        for key in d.keys():
            l.append(d[key])
        return l