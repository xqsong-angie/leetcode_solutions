#20260806

#错：全局堆
class Leaderboard:
    """
    @param player_id: ID of a player.
    @param score: Score of the player.
    @return: nothing
    """
    def __init__(self):
        self.leaderboard=defaultdict(int)
        self.heap=[]#🔥全局堆的坏处：调用 top(k) 时，他一个人可能会占据前 k 名里的好几个名额，两次调用top拿出来答案不一样
    def add_score(self, player_id: int, score: int):
        # --- write your code here ---
        if player_id in self.leaderboard:
            self.leaderboard[player_id]+=score
        else:
            self.leaderboard[player_id]=score
        heappush(self.heap,(-self.leaderboard[player_id],player_id))


    """
    @param k: Top k players.
    @return: Summary of the scores of the top k players.
    """
    def top(self, k: int) -> int:
        # --- write your code here ---
        sum_k=0
        for _ in range(k):
            if self.heap:
                sum_k+=(-heappop(self.heap)[0])

    """
    @param player_id: ID of a player.
    @return: nothing
    """
    def reset(self, player_id: int):
        # --- write your code here ---
        self.leaderboard #🔥reset无法从堆中删除特定的player_id元素

#对：动态堆
import heapq
from collections import defaultdict

class Leaderboard:
    def __init__(self):
        # 只用字典维护状态
        self.leaderboard = defaultdict(int)

    def add_score(self, player_id: int, score: int):
        # O(1) 操作，直接累加
        self.leaderboard[player_id] += score

    def top(self, k: int) -> int:
        # O(N log k) 操作
        # nlargest 会遍历字典所有的 values，并返回最大的 k 个组成的列表
        top_k_scores = heapq.nlargest(k, self.leaderboard.values()) #对self.leaderboard.values()数组建动态堆
        return sum(top_k_scores)

    def reset(self, player_id: int):
        # O(1) 操作，直接删除该玩家的记录
        if player_id in self.leaderboard:
            del self.leaderboard[player_id]