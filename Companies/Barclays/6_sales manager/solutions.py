def get_max_palindromic_list(salesData):
    n = len(salesData)
    if n <= 1:
        return salesData

    left, right = 0, n - 1
    left_sum = salesData[left]
    right_sum = salesData[right]

    left_res = []   # 保存回文列表的左半部分
    right_res = []  # 保存回文列表的右半部分

    while left < right:
        if left_sum == right_sum:
            # 找到匹配项，分别保存到左右两侧
            left_res.append(left_sum)
            right_res.append(right_sum)

            # 推进指针并更新当前和
            left += 1
            right -= 1
            left_sum = salesData[left]
            right_sum = salesData[right]

        elif left_sum < right_sum:
            # 左侧和偏小，合并左侧下一个元素
            left += 1
            left_sum += salesData[left]

        else:
            # 右侧和偏小，合并右侧上一个元素
            right -= 1
            right_sum += salesData[right]

    # 处理指针相遇的情况
    if left == right:
        # 指针刚好重合在同一个位置，将该元素放入中间
        left_res.append(salesData[left])
    elif left_sum == right_sum:
        # 最后的合并刚好在中间相等
        left_res.append(left_sum)

    # 最终结果 = 左半部分 + 翻转后的右半部分
    final_res = left_res + right_res[::-1]
    return final_res
