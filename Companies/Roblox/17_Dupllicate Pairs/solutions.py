def count_subarrays_with_k_pairs(numbers: list[int], k: int) -> int:
    n = len(numbers)
    left = 0
    total_pairs = 0
    counts = {}
    valid_subarrays_count = 0
    
    for right in range(n):
        val = numbers[right]#窗口右侧的idx
        counts[val] = counts.get(val, 0) + 1#见到一个val就+1
        
        # Every time a number's count becomes even, we gain a new pair
        if counts[val] % 2 == 0:
            total_pairs += 1
            
        # Shrink the window from the left while maintaining total_pairs >= k
        while total_pairs >= k:
            left_val = numbers[left]#🔥拿到删去的是什么元素
            # If removing this element reduces a pair, update total_pairs
            if counts[left_val] % 2 == 0:
                total_pairs -= 1
            counts[left_val] -= 1
            left += 1
            
        # 🔥All subarrays ending at 'right' starting at indices 0, 1, ..., left - 1 are valid
        valid_subarrays_count += left

    return valid_subarrays_count