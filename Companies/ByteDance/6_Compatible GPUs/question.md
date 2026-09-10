5. Compatible GPUs

ByteDance is planning to buy some GPUs for training their new computer vision models using them. They have 2 clusters on which all the models are saved. There are n GPUs available, where the cost of the i-th GPU is represented by array element cost[i]. Also, there are two arrays compatible1 and compatible2 each containing n integers, where each integer is either 0 or 1, representing the following:

- If compatible1[i] = 1, then the i-th GPU is compatible with cluster 1, else it is not compatible with cluster 1.
- If compatible2[i] = 1, then the i-th GPU is compatible with cluster 2, else it is not compatible with cluster 2.

The company wants to buy the GPUs such that there are at least a min_compatible number of GPUs compatible with each of cluster 1 and cluster 2.
Given n GPUs, an integer min_compatible, and three arrays cost, compatible1 and compatible2, find the minimum possible cost of GPUs such that there are at least a min_compatible number of GPUs compatible with each of cluster 1 and cluster 2. Return -1 if it is not possible to buy the GPUs satisfying the above condition.


Example

Given, cost = [2, 4, 6, 5], compatible1 = [1, 1, 1, 0], compatible2 = [0, 0, 1, 1], and min_compatible = 2.

Some of the ways of buying the GPUs are explained below:

GPUs Bought (Indices 0-based) | Cost    | Is Valid?
------------------------------|---------|--------------------------------------------------
[0, 2]                        | 2 + 6 = 8 | Indices GPUs Compatible with cluster 1 = [0, 2].
                              |         | Indices GPUs Compatible with cluster 2 = ...