class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        q = []

        def dfs(opene, close):
            if opene == close == n: 
                res.append("".join(q))
                return


            if opene < n:
                q.append("(")
                dfs(opene+1, close)
                q.pop()
            if close < opene:
                q.append(")")
                dfs(opene, close+1)
                q.pop()

        dfs(0, 0)
        return res





        