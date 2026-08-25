Imagine there is a group chat with many users writing messages. The content of messages includes text and mentions of other users in the chat. Mentions in the group chat are formatted as strings starting with `@` character and followed by at least one id separated by commas. An id is formatted as a string starting with `id` and followed by a positive integer from `1` to `999`.

For example:

* `"This is an ex@mple with no mentions@"`
* `"This is an example with @id1 one mention of one user"`
* `"This is an example with @id1,id123,id983 one mention of three users"`
* `"This is an example with @id1,id123,id983 several mentions of several users @id239"`

Now, imagine you are given two arrays of strings titled `members` and `messages`. Your task is to calculate the mention statistics for the group chat. In other words, count the number of messages that each chat member is mentioned in. Chat members mentioned multiple times in a message should be counted only once per message.

Return the mention statistics in an array of strings, where each string follows this format: `"[user id]=[mentions count]"`. The array should be sorted by mention count in descending order, or in case of a tie, lexicographically by `user id` in ascending order.

It is guaranteed that proper ids will be used for each mention. Additionally, all mentions will be preceded by and followed by a space, unless they are located at either the beginning or end of the message. Note that the `@` character is still allowed to be included