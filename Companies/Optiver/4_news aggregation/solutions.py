from collections import defaultdict
class NewsProvider:
    def __init__(self):
        self.subscription={}
        self.news={}#news received
        self.news_sent=set()

    def AddSubscription(self, id: int, minInterest: int, maxNewsPerSecond: int, topics: list[str]) -> bool:
        self.subscription[id]={"minInterest":minInterest,"maxNewsPerSecond":maxNewsPerSecond,"topics":topics}
        return True
        #🔥什么时候能执行不成功return False?
    
    def RemoveSubscription(self, id: int) -> bool:
        if id in self.subscription.keys():
            self.subscription.remove(id)#🔥用pop(id),dict没有remove
            return True
        else:
            return False

    def NewsReceived(self, id: int, timestamp: float, interest: int, topics: list[str]) -> bool:
        if id in self.news_sent:
            return False
        self.news_sent.add(id)
        self.news[id]={"timestamp":timestamp,"interest":interest,"topics":topics}
        return True
    
    def Publish(self, timestamp: float, maxAge: float) -> dict[int, list[int]]:
        res=defaultdict(list)
        valid_news=[]#所有合法的新闻
        for k,v in self.news.items():
            if timestamp-maxAge<=v["timestamp"]<=timestamp:
                valid_news.append(v["interest"],v["timestamp"],k,set(v["topics"]))
        valid_news.sort(key=lambda x:(-x[0],x[1],-x[2]))
        for s in valid_news:#s:(interest,timestamp,news_id,topics)
            for k,v in self.subscription.items():
                if v["minInterest"]<=s[0]:
                    for topic in v["topics"]:
                        if topic in s[3] and len(res[s[2]])<=maxAge*v["maxNewsPerSecond"]:
                            res[s[2]].append(k)
        return res#🔥这个函数会严重超时

#参考答案
from collections import defaultdict

class NewsProvider:
    def __init__(self):
        # id -> {"minInterest": int, "maxNewsPerSecond": int, "topics": set}
        self.subscriptions = {}
        # id -> {"timestamp": float, "interest": int, "topics": set}
        self.news = {}
        # 记录所有已经接收过的 news_id
        self.received_news_ids = set()

    def AddSubscription(self, id: int, minInterest: int, maxNewsPerSecond: int, topics: list[str]) -> bool:
        # 如果 id 已存在则覆盖更新，均属于成功操作
        self.subscriptions[id] = {
            "minInterest": minInterest,
            "maxNewsPerSecond": maxNewsPerSecond,
            "topics": set(topics)  # 转成 set 方便做高效集合交集计算
        }
        return True

    def RemoveSubscription(self, id: int) -> bool:
        if id in self.subscriptions:
            del self.subscriptions[id]
            return True
        return False

    def NewsReceived(self, id: int, timestamp: float, interest: int, topics: list[str]) -> bool:
        # id 如果已经使用过，操作失败
        if id in self.received_news_ids:
            return False
            
        self.received_news_ids.add(id)
        self.news[id] = {
            "timestamp": timestamp,
            "interest": interest,
            "topics": set(topics)
        }
        return True

    #🔥不要顺着题目思路写，限流（Quota / Rate Limit）的约束主体是“订阅者（Subscriber）”，而不是“新闻（News）”！，所以反过来才是优化性能的关键
    def Publish(self, timestamp: float, maxAge: float) -> dict[int, list[int]]:
        res = defaultdict(list)
        min_valid_time = timestamp - maxAge

        # 1. 过滤出在 [timestamp - maxAge, timestamp] 时间窗口内的未过期新闻
        valid_news = []
        expired_ids = []
        for news_id, news_info in self.news.items():
            if min_valid_time <= news_info["timestamp"] <= timestamp:
                valid_news.append({
                    "id": news_id,
                    "interest": news_info["interest"],
                    "timestamp": news_info["timestamp"],
                    "topics": news_info["topics"]
                })
            elif news_info["timestamp"] < min_valid_time:
                expired_ids.append(news_id)

        # 🔥内存优化：清理彻底过期的历史新闻
        for e_id in expired_ids:
            del self.news[e_id]

        # 2. 全局优先级排序：highest interest -> oldest timestamp -> highest id
        valid_news.sort(key=lambda x: (-x["interest"], x["timestamp"], -x["id"]))

        # 3. 按订阅者处理限流与匹配 (按人取新闻)
        for sub_id, sub_info in self.subscriptions.items():
            quota = int(maxAge * sub_info["maxNewsPerSecond"])
            delivered_count = 0
            
            for item in valid_news:
                if delivered_count >= quota:
                    break  # 已满额度，停止推送该订阅者
                
                # 判断兴趣值与主题是否有交集
                if item["interest"] >= sub_info["minInterest"]:
                    # 🔥判断交集逻辑：set & set 比 list 循环快很多
                    if item["topics"] & sub_info["topics"]:#（&是按位运算符）
                        res[item["id"]].append(sub_id)
                        delivered_count += 1

        return dict(res)