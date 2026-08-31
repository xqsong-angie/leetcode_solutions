from collections import Counter,defaultdict
class Solution:
    def solution(self,wordSet,sentences):
        res=[]
        freq=defaultdict(int)
        for i in range(len(wordSet)):
            tab=Counter(wordSet[i])
            freq(tab)+=1#🔥counter对象不可哈希
        for i in range(len(sentences)):
            lst=sentences[i].split()
            product=1
            for j in lst:
                tab2=Counter(j)
                product*=freq[tab2]
            res.append(product)
        return res
    
#对：🔥两个单词如果是 Anagram（变位词），只要将它们的字母按字典序排序，排序后的字符串就会完全相同（例如 'listen' 和 'silent' 排序后都是 'eilnst'）
class Solution:
    def countSentences(self, wordSet: list[str], sentences: list[str]) -> list[int]:
        # 1. 统计 wordSet 中每个单词排序后的 key 的出现频率
        freq = defaultdict(int)
        for word in wordSet:
            # 将单词按字母排序作为哈希表的 key
            key = "".join(sorted(word))
            freq[key] += 1

        res = []

        # 2. 遍历每个句子，运用乘法原理计算总方案数
        for sentence in sentences:
            words = sentence.split()
            product = 1
            for word in words:
                key = "".join(sorted(word))
                # 如果 wordSet 中有这个变位词组，选择数就是 freq[key]
                # 如果没有（以防万一），保持单词原样，选择数为 1
                count = freq.get(key, 1)
                product *= count
                
            res.append(product)

        return res

# 验证 Sample Input
sol = Solution()
wordSet = ['the', 'bats', 'tabs', 'in', 'cat', 'act']
sentences = ['cat the bats', 'in the act', 'act tabs in']
print(sol.countSentences(wordSet, sentences))  # 输出: [4, 2, 4]