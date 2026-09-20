Question 1

You are implementing the firmware controller that prevents a multi-core microprocessor from overheating. Every core runs a workload that produces heat proportional to its configured load, and all cores share a fixed cooling capacity. The operating system (OS) is in charge of assigning workloads via SetCoreLoad, and drives the controller forward via Tick on a cadence of its choosing to learn how each core's status has changed.

Scoring
The list below shows the test-case categories used to evaluate your submission, roughly ordered from most to least impactful. Use this as guidance for where to invest effort; categories are intentionally broad and can overlap, so don't over-optimize for labels.

State Management
Core Logic
Edge Cases
Scalability/Performance

Overview
Implement the OverheatPreventionController class with the following operations:

init — (constructor) initializes the controller with its cooling capacities and cores.
SetCoreLoad — lazily updates a core's configured workload; can also restart a shut down core.
Tick — advances the controller's internal state to the given timestamp, processes any pending load changes and returns the cores whose status has changed since the previous Tick.

The controller doesn't have temperature sensors; instead, it must calculate the temperature of each core based on the configured loads and the cooling layout, as defined in Thermal Dynamics. Loads are given in watts (W).

Functions

def __init__(self, passive_cooling_capacity: float, active_cooling_capacity_per_core: float, core_ids: list[str]) -> None:
    ...

This represents the constructor of the class in whatever programming language being used.
Initializes the controller with the given passive_cooling_capacity (the shared passive cooling budget, in watts), active_cooling_capacity_per_core (the dedicated per-core active-cooling capacity, in watts, applied uniformly to every core when engaged), and the list of valid core_ids.
All cores start at ambient temperature (20.0°C), running, with load 0 and active cooling off (i.e., status idle, see Tick below).

You may assume:
1 <= R <= 2**10, where R is the total number of cores.
passive_cooling_capacity > 0 and active_cooling_capacity_per_core > 0.
All core identifiers are unique.

def SetCoreLoad(self, timestamp: float, core_id: str, load_watts: float) -> None:
    ...

Records a new configured load for the given core. Performs no thermal arithmetic. The new load only takes effect at the next Tick.
If two or more SetCoreLoad calls land on the same core between two Ticks, only the last one takes effect.
If the core is currently shut down, this call also acts as a manual restart attempt: it will restart the core with the new load, but only if the core's temperature observed at the next Tick is strictly below 50°C. Otherwise the restart is discarded and the core stays shut down with load 0 — restarting later requires another SetCoreLoad call.
If the core is currently running, the new load is simply recorded and processed normally at the next Tick.

You may assume core_id always exists and load_watts is always within [0, 2**15].

def Tick(self, timestamp: float) -> list[str]:
    ...

It does, in order:
1. Advances the controller to timestamp in a single step. See Thermal Dynamics for how temperatures evolves.
2. Shuts down any core whose temperature has reached 80°C (its load is cleared to 0).
3. Processes any pending load changes, including restart attempts on shut down cores.
4. Decides which cores should have active cooling engaged for the upcoming interval. See Active Cooling for details.

Returns the cores whose status has changed since the previous Tick (or diverged from the initial state), where a core's status is one of:
idle — running, active cooling off.
cooling — running, active cooling engaged for the upcoming interval.
shutdown — shut down.

Each entry of the returned list has the format "core_id=status". The list is sorted alphabetically by core_id. An empty list means nothing has changed.

Thermal Dynamics
At every Tick, the controller first computes each core's temperature at the given timestamp.
A core's temperature is determined as follows:

Every core's temperature evolves linearly at a rate of 0.02°C/s per watt of net heat balance, positive or negative. Net heat balance is the core's load minus all its allocated cooling. When cooling down, a core's temperature will never drop below 20.0°C.
The cooler distributes its effective passive cooling capacity across the cores according to their passive cooling demand. The demand is load + 2 W per core, where +2 W represents the maximum passive heat dissipation per core. The passive cooling distribution is as follows:
If the total passive demand fits within the effective passive capacity, every core's demand is fully met.
Otherwise, capacity is distributed proportionally to each core's demand.
The cooler's effective passive cooling capacity depends on whether active cooling was engaged by the previous Tick. The effect is described below.

Active Cooling
At the end of each Tick, the controller decides which cores should have active cooling engaged until the next Tick, when the decision will be reassessed from scratch. Active cooling works as follows:

Each core has a dedicated active-cooling channel that delivers exactly active_cooling_capacity_per_core watts on top of the passive cooling when engaged on that core.
Active cooling is expensive, therefore it should be engaged on as few cores as possible to satisfy these rules:
- Any core whose temperature is rising faster than 0.5°C/s must be engaged.
- Any core whose temperature is above 60°C must be engaged.

When active cooling is on, the passive cooler vibrates and runs less efficiently. The efficiency decreases proportionally to the number of cores that have active cooling engaged. When k cores are actively cooling, the total passive cooling capacity is reduced by vibration_penalty(k) percent, where:
vibration_penalty(0) = 0
vibration_penalty(k) = sum(10 / Fib_i for i in range(1, k + 1)), where Fib_i is the i-th term of the sequence 1, 2, 3, 5, 8, 13, ... (Fibonacci, starting from its second term).

Because engaging active cooling on a core increases the vibration penalty for everyone, it can in turn lift other cores' rates above 0.5°C/s and trigger their engagement as well within the same interval.

Constraints

All timestamps are globally ever-increasing. Operations will never arrive out of order.
Timestamps are seconds since the Unix Epoch (Jan 1, 1970 UTC), as floating-point values with millisecond precision. They are positive and fit into 32 bits.
Loads and cooling capacities are in watts, as floating-point values with milliwatt precision (3 decimal places).
State transition thresholds and the active-cooling rate threshold are exact. Test inputs are constructed so that observed temperatures and rates stay clear of these thresholds by a margin that exceeds floating-point precision.
1 <= N <= 2**10, where N is the total number of operations given to the program.