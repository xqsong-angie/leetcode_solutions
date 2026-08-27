**2. How many Sentences?**

Given an array of words and an array of sentences, determine which words are anagrams of each other. Calculate how many sentences can be created by replacing any word with one of its anagrams.

**Example**
wordSet = ['listen', 'silent', 'it', 'is']
sentence = 'listen it is silent'

Determine that listen is an anagram of silent. Those two words can be replaced with their anagrams. The four sentences that can be created are:

* listen it is silent
* listen it is listen
* silent it is silent
* silent it is listen

**Function Description**
Complete the countSentences function in the editor below.

countSentences has the following parameters:

* string wordSet[n]: an array of strings
* string sentences[m]: an array of strings

**Returns**

* int[]: an array of m integers that denote the number of sentences that can be formed from each sentence

**Constraints**

* 0 < n <= 10^5
* 1 <= length of each word <= 20
* 1 <= m <= 1000
* 3 <= words in a sentence <= 20

---

**Sample Input**

STDIN:
6
the
bats
tabs
in
cat
act
3
cat the bats
in the act
act tabs in

Function:
n = 6
wordSet = ['the', 'bats', 'tabs', 'in', 'cat', 'act']
m = 3
sentences = ['cat the bats', 'in the act', 'act tabs in']

**Sample Output**
4
2
4

**Explanation**
Sentence 1: For the sentence 'cat the bats', the sentences that can be formed are:

* cat the bats
* act the bats
* cat the tabs
* act the tabs

Sentence 2: For the sentence 'in the act', the sentences that can be formed are:

* in the act
* in the cat