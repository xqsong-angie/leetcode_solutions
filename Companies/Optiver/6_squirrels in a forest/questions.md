Researchers are studying the behavior of squirrels in a forest, where they compete to hide and collect nuts in hidden locations. You are tasked with implementing a tracker that can simulate this behavior. Your system is initialized with a list of locations and their capacities, and should support the following actions:
- Register when a nut has been hid by a squirrel in a location.
- Register how nuts are retrieved by a squirrel from a location.

Problem Statement

Complete the functions described below in the SquirrelResearch class. Keep in mind that:
- If any constraint is violated when performing an operation, the operation must fail.
- If a constraint is said to be "guaranteed", you may assume it is never violated.
- Action functions include a timestamp indicating when such action has taken place. They are guaranteed to be globally ever increasing.
- Timestamps are represented as number of seconds since the Unix Epoch (Jan 1, 1970 UTC), using floating-point values valid to the millisecond precision. They are guaranteed to be positive numbers and fit into 32 bits.
- Weights are represented in grams, using floating-point values valid to the milligram precision.

Guaranteed input constraints:
- 1 < N < 2**15, where N is the total number of instructions given to the program.

Functions:

def __init__(self, locations: dict[str, int]) -> None:
    ...

Initializes the class with all available hiding locations. This represents the constructor of the class in whatever programming language being used.
locations is a map where key is the location's unique identifier, and the value is the location's number of levels.
Hiding locations are shaped like a cone, forming storage levels that grow in size according to the Fibonacci sequence starting from the 3rd digit. For example, a location with 3 levels can fit up to 6 nuts: 1 at deepest level, 2 at the middle level, and 3 at the top level.

Guaranteed input constraints:
- 1 <= levels < 2**5
- 1 <= Q < 2**20, where Q is the length of locations.

def HideNut(self, timestamp: float, location_id: str, nut_id: str, nut_weight: float, time_to_expire: float) -> bool:
    ...

A squirrel attempts to hide a nut in a location. Returns True if the operation succeeds, and False otherwise.
Locations are filled from the deepest level upwards. Only once a level is completely filled, nuts start filling up the next level.
nut_id is a unique string identifier for a nut. If a nut is already hidden (anywhere), the operation fails.
If the location is full or invalid, the operation fails.
time_to_expire represents the time it takes for this nut to expire, starting at timestamp. In other words, a nut is considered expired immediately after timestamp + time_to_expire. It's represented in seconds using floating-point values valid to the millisecond precision.

Input constraints:
- 0 < nut_weight < 20

def RetrieveNuts(self, timestamp: float, location_id: str, max_squirrel_capacity_in_nuts: int) -> list[str]:
    ...

A squirrel attempts to retrieve nuts from a location. Returns a list with the nut_ids retrieved (in order of retrieval) if the operation succeeds, and an empty list otherwise.
max_squirrel_capacity_in_nuts indicates the maximum number of nuts the current squirrel can retrieve.
Nuts are retrieved first by level, starting from the upmost level with nuts. Per level, heavier nuts are retrieved first.
If the upmost level is occupied by less than 50% of its total capacity, the next level becomes reachable and the squirrel will prefer nuts from there if they're heavier. If there's a tie on weight, the nut with the smallest id (alphabetically) is retrieved first.
Every time a nut is taken out of a level that's not the upmost level with nuts, the lightest nut from the level above falls into its place.
If an expired nut is retrieved, it gets immediately discarded by the squirrel.
Retrieved and discarded nuts are removed from the location. Once retrieved, a nut_id may be used again to identify other nuts.
If the location is empty or invalid, the operation fails.

Input constraints:
- 1 <= max_squirrel_capacity_in_nuts < 2**10