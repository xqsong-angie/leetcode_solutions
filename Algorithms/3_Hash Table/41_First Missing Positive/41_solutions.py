#20260806
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Find the first missing positive integer in an unsorted array.
        Uses cyclic sort to place each positive integer at its correct position.
        Time: O(n), Space: O(1) (in-place hash)
        """
        n = len(nums)
      
        # Phase 1: Place each positive integer at its correct position
        # For a positive integer k (where 1 <= k <= n), place it at index k-1
        for i in range(n):
            # Keep swapping current element to its correct position
            # until current position has correct element or invalid element
            while (1 <= nums[i] <= n and #短路求值，如果1 <= nums[i] <= n，则nums[i] - 1最大为n-1，不会越界
                   nums[i] != nums[nums[i] - 1]):#我们可以确定，数组nums里面最多有n个positive integer(算上重复的)，最终结果最大n+1
                # Calculate target index for current element 所以我们用idx作原地哈希的key
                target_index = nums[i] - 1
                # Swap current element with element at target position
                nums[i], nums[target_index] = nums[target_index], nums[i]
      
        # Phase 2: Find the first position where element doesn't match expected value
        # Position i should contain value i+1
        for i in range(n):
            if nums[i] != i + 1:#说明哪里空了
                return i + 1
      
        # All positions [0, n-1] contain correct values [1, n]
        # So the first missing positive is n+1
        return n + 1#最坏的结果