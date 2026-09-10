Adison works for a Client servicing company whose head office is located in zone '1' in a city. He has to provide service to the customer in a zone and return back to head office after servicing each complaint. Since he is not well, he likes to optimize the rest time after each service he provides. Hence, he tries to locate the minimum distance between the head office and the target zone. There are N zones, numbered 1 to N, connected by M bidirectional roads such that every zone is connected to that head office either directly or via any other zone. Adison is given a list of M pairs of two zones [A, B] and the time T needed to reach from zone A to zone B.

To service Q complaints in the order in which they have been assigned, he is given the name of the zone X and the time limit K in which he can service a complaint to that zone and return to the head office. If he is able to find the shortest route from zone '1' and this save time, then he can take good rest. If K units of time are not sufficient to visit the zone X and return back to the head office, he will not be able to service a complaint in that zone and the rest time will also be zero.

Write an algorithm to compute Adison's maximum rest time in each service for Q complaints given in a day.

Input
The first line of the input consists of an integer numZones(N), representing the number of zones.
The second line consists of two space-separated integers numRoads(M) and constX representing roads and constX is always 3.
The next M lines consist of constX(which is always 3) space-