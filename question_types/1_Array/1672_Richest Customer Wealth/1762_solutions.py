#20260610
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n=len(accounts)
        max_wealth=0
        for i in range(n):
            max_wealth=max(max_wealth,sum(accounts[i]))
        return max_wealth
