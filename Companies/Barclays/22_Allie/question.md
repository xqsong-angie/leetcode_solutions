Allie is working on a system that can allocate resources to the applications in a manner efficient enough to allow the maximum number of applications to be executed. There are N number of applications and each application is identified by a unique integer ID (1 to N). Only M types of resources are available with a unique resourceID. Each application sends a request message to the system. The request message includes the information regarding the request time, the execution ending time, and the type of resource required for execution. Time is in the MMSS format where MM is minutes and SS is seconds.

If more than one application sends a request at the same time then only one application will be approved by the system. The denied requests are automatically destroyed by the

Input
The first line of the input consists of two space-separated integers num and constX, representing the number of applications (N) and constX is always 3.
The next N lines consist of constX space-separated integers representing the request time, the execution ending time, and the resourceID of the resource required by each application for successful execution.

Output
Print an integer representing the maximum number of applications that are executed successfully by the system.

Constraints
1 ≤ num ≤ 10^3