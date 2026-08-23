Think about a team chat with numerous users writing messages in it. The chat supports two types of actions:  

"MESSAGE" - Messages a set of users. The format looks as follows: ["MESSAGE", "<timestamp>", "<mentions>"]. Mentions string can contain the following space-separated tokens:  

id<number>, where <number> is an integer in range [1:999] - mentioning of individual users  

ALL - mentioning all users  

HERE - mentioning active users  

"OFFLINE" - Makes a user with a given id inactive for 60 time ticks - the user will be active again at time <timestamp> + 60. It is guaranteed that the user with given <id> will be active when this action is applied. The format looks as follows: ["OFFLINE", "<timestamp>", "<id>"], where id is a single individual mention.  

For members = ["id42", "id158", "id23"] and
events = [
["MESSAGE", "0", "ALL id158 id42"],
["OFFLINE", "1", "id158"],
["MESSAGE", "2", "id158 id158"],
["OFFLINE", "3", "id23"],
["MESSAGE", "60", "HERE id158 id42 id23"],
["MESSAGE", "61", "HERE"]
]
the output should be solution(members, events) = ["id158=4", "id23=2", "id42=3"] !