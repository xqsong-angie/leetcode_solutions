Problem: News Aggregation Service

As the provider of a news aggregation service, you aim to provide your customers with a system that is as easy to use as possible. There are many different news providers, and it is tedious for users to subscribe to all of them manually, so you want to provide a single subscription that manages all the news providers for each customer.

Each subscriber is only interested in a certain set of topics, and should only receive news about those topics. Each news item has an interest score and each subscriber nominates their minimum interest score. A subscriber should not be sent news that has a score lower than the subscriber's minimum.

The system may have to handle a lot of data and subscriptions, so it must be robust and not overload subscribers with too much data. We then choose to decouple the news input feed from the output towards the subscribers, giving more control to the system.

Problem Statement:
Complete the functions described below in the NewsProvider class. Keep in mind that:
- If any constraint is violated when performing an operation, the operation must fail.
- If a constraint is said to be "guaranteed", you may assume it is never violated.
- Timestamps are represented as number of seconds since the Unix Epoch (Jan 1, 1970 UTC), using floating-point values valid to the millisecond precision. They are guaranteed to be positive numbers and fit into 32 bits.

Guaranteed Input Constraints:
- 0 < N < 2**15, where N is the total number of instructions given to the program.

--------------------------------------------------------------------------------
Class & Function Signatures:

class NewsProvider:

    def AddSubscription(self, id: int, minInterest: int, maxNewsPerSecond: int, topics: list[str]) -> bool:
        """
        Register a new subscription for upcoming news on certain topics.
        Returns True if the operation succeeds, and False otherwise.

        - id: Unique identifier of the subscription. If a subscription with the same id already exists, 
              the subscription must be updated with the new parameters.
        - minInterest: Minimum interest score desired (inclusive).
        - maxNewsPerSecond: Maximum number of news items this subscription can receive per second. 
                            This constraint is based on a rolling window, i.e., it starts counting since the last published timestamp.
        - topics: List of news topics this subscription should consider.

        Input Constraints:
          0 <= id < 2**32
          0 <= minInterest < 2**32
          1 <= maxNewsPerSecond <= 2**12
          0 <= len(topics) < 2**10
        """
        pass

    def RemoveSubscription(self, id: int) -> bool:
        """
        Removes an existing subscription from the system. 
        Returns True if the operation succeeds, and False otherwise.

        - id: Unique identifier of the subscription to be removed. If it doesn't exist, the operation fails.
        """
        pass

    def NewsReceived(self, id: int, timestamp: float, interest: int, topics: list[str]) -> bool:
        """
        Indicates news on given topics have been received at a given timestamp. 
        Returns True if the operation succeeds, and False otherwise.

        - id: Unique identifier of these news. If it has already been used, the operation fails.
        - interest: Interest score of these news.

        Input Constraints:
          0 <= id < 2**32
          0 <= interest < 2**32
          0 <= len(topics) < 2**10
        """
        pass

    def Publish(self, timestamp: float, maxAge: float) -> dict[int, list[int]]:
        """
        Computes the news to be published at the given timestamp. 
        Returns a map of news ids to subscription ids, i.e., all subscriptions to be notified per news id. 
        If the operation fails, returns an empty map.

        Rules:
        - If needed, news must be prioritized first by highest interest score, then oldest timestamp, then highest id.
        - A subscriber must never receive the same news twice.
        - maxAge: Maximum age of news to be published at this time (in seconds).

        Guaranteed Input Constraints:
          timestamp is ever increasing for calls of this function.

        Input Constraints:
          0 < maxAge < 2**32
        """
        pass

--------------------------------------------------------------------------------
Input Format for Custom Testing:

Each line of input begins with a keyword followed by one or more parameters separated by whitespace:
1. "subscribe" -> AddSubscription(id, minInterest, maxNewsPerSecond, topics...)
2. "unsubscribe" -> RemoveSubscription(id)
3. "news" -> NewsReceived(id, timestamp, interest, topics...)
4. "publish" -> Publish(timestamp, maxAge)

--------------------------------------------------------------------------------
Sample Case 1:

Sample Input:
subscribe 1 5 2 radio television
subscribe 2 7 3 cable
news 10 100 4 television
news 11 100 5 television cable
news 12 150 7 radio streaming
publish 200 100

Sample Output:
subscribed=True
subscribed=True
news_received=True
news_received=True
news_received=True
publish:
- news=11 to [1]
- news=12 to [1]

Explanation Case 1:
Two subscribers:
- Sub 1: Min Interest = 5, Max News/s = 2, Topics = [radio, television]
- Sub 2: Min Interest = 7, Max News/s = 3, Topics = [cable]

Three news items received:
- News 10: Timestamp = 100, Interest = 4, Topics = [television]
- News 11: Timestamp = 100, Interest = 5, Topics = [television, cable]
- News 12: Timestamp = 150, Interest = 7, Topics = [radio, streaming]

Publish Call: timestamp = 200, maxAge = 100
- All news (10, 11, 12) are within maxAge (200 - timestamp <= 100).
- News 10: Interest score 4 < Sub 1's min 5, not published.
- News 11: Matches Sub 1 (Interest 5 >= 5) and Sub 2 (Interest 5 < Sub 2's min 7, skipped).
- News 12: Matches Sub 1 (Interest 7 >= 5).

--------------------------------------------------------------------------------
Sample Case 2:

Sample Input:
subscribe 1 5 2 technology
subscribe 2 5 2 technology sport
subscribe 3 1 100 sport
news 1 10 4 sport
news 2 20 4 technology
news 3 30 5 sport
news 4 40 5 technology
news 5 50 6 sport technology
news 6 1003 5 technology
news 7 1004 5 technology sport
publish 1020 1000

Sample Output:
subscribed=True
subscribed=True
subscribed=True
news_received=True
news_received=True
news_received=True
news_received=True
news_received=True
news_received=True
news_received=True
publish:
- news=3 to [2, 3]
- news=4 to [1]
- news=5 to [1, 2, 3]
- news=7 to [3]

Explanation Case 2:
Subscribers:
- Sub 1: Min Interest = 5, Max News/s = 2, Topics = [technology]
- Sub 2: Min Interest = 5, Max News/s = 2, Topics = [technology, sport]
- Sub 3: Min Interest = 1, Max News/s = 100, Topics = [sport]

News Items Evaluation (Publish at 1020, maxAge 1000):
1. News 1 (ts=10): Age 1010 > maxAge 1000, expired.
2. News 2 (ts=20, int=4): Interest score 4 < minInterest 5 for Sub 1 & 2.
3. News 3 (ts=30, int=5): Matches Sub 2 and 3.
4. News 4 (ts=40, int=5): Matches Sub 1 and 2.
5. News 5 (ts=50, int=6): Matches Sub 1, 2, and 3.
6. News 6 (ts=1003, int=5): Matches Sub 1 and 2.
7. News 7 (ts=1004, int=5): Matches Sub 1, 2, and 3.

Per-Subscriber Filtering & Rate Limits (Max 2 news/s for Sub 1 & Sub 2):
- Candidate List for Sub 1: News 5 (int=6), News 4 (int=5), News 6 (int=5), News 7 (int=5)
  Sorted by Priority -> [News 5, News 4, News 7, News 6]
  Quota limit = 2 -> Takes News 5 and News 4.
- Candidate List for Sub 2: News 5 (int=6), News 3 (int=5), News 4 (int=5), News 7 (int=5)
  Sorted by Priority -> [News 5, News 3, News 4, News 7]
  Quota limit = 2 -> Takes News 5 and News 3.
- Candidate List for Sub 3: Quota = 100 -> Takes News 3, 5, 7.