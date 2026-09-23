Problem: Balloon Festival Simulation

You are tasked with implementing a simulation system for a hot air balloon festival. The system must track multiple balloons, their altitudes, stability, and the effect of varying wind speeds over time.

Core Rules:

Initialization:
You are given a list of balloon names at initialization. Only these balloons may participate in the simulation. Any action involving an unknown balloon name should fail.

Stability:
Balloons are stable by default when they first ascend. A balloon becomes unstable if the total wind speed at its altitude exceeds 15 m/s.
Once unstable, a balloon regains stability only if:
- It remains at the same altitude, and
- The total wind speed stays strictly <= 15 m/s for 300 continuous seconds.

Wind Contribution:
Wind is defined at center altitudes with a specific speed. The effect of wind at a balloon's altitude h is calculated by:

    W(h) = W_center / (1 + ((h - centerAltitude) / 100)**2)

The total wind speed is the sum of contributions from all active wind centers.

Operations:

- balloon_ascended(timestamp, name, altitude):
  The balloon ascends to the specified altitude. Stable by default, then immediately checked for wind instability. Returns True if successful, False if timestamp is invalid or balloon is unknown.

- balloon_descended(timestamp, name):
  The balloon descends to the ground. Stability resets to default. Returns False if the balloon was not flying or timestamp is invalid.

- set_wind_speed(timestamp, centerAltitude, windSpeed):
  Sets or updates a wind center at a given altitude. This overwrites any previous wind speed at that center. After updating, all balloons are re-evaluated for stability.

- inspect_balloons(timestamp):
  Returns the names of all stable balloons at the highest stable altitude (ties allowed). If no stable balloons are flying, return an empty list.

Timestamps:
All operations have strictly increasing timestamps. If an operation has a timestamp <= the previous timestamp, it must return False (or an empty list for inspect_balloons).

Output Requirements:
inspect_balloons must list balloon names in the same order they were provided during initialization.