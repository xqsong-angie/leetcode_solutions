**2. Encircular**

Build a computer simulation of a mobile robot. The robot moves on an infinite plane, starting from position $(0, 0)$. Its movements are described by a command string consisting of one or more of the following three letters:

* *G* instructs the robot to move forward one step.
* *L* instructs the robot to turn left in place.
* *R* instructs the robot to turn right in place.

The robot performs the instructions in a command sequence in an infinite loop. Determine whether there exists some circle such that the robot always moves within the circle.

Consider the commands R and G executed infinitely. A diagram of the robot's movement looks like:

```text
RG → RG
 ↑    ↓
RG ← RG

```

The robot will never leave the circle.

**Function Description**

Complete the function *doesCircleExist* in the editor below. The function must return an array of $n$ strings either *YES* or *NO* based on whether the robot is bound within a circle or not, in order of test results.