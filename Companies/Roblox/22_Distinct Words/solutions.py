def solution(matrix: list[list[str]], words: list[str]) -> int:
    R = len(matrix)
    C = len(matrix[0])
    total_count = 0

    def get_char(r, c):
        return matrix[r][c]

    for word in words:
        L = len(word)

        # 遍历所有可能的起点 (r, c)
        for r in range(R):
            for c in range(C):
                # ----------------------------------------------------
                # 1. 水平方向搜索 (起始必须是右 -> 允许折返向左)
                # ----------------------------------------------------
                # 枚举向右走的步数 step_right (从 0 到 L-1)
                for step_right in range(L):
                    # 向右到达的最远列
                    max_c = c + step_right
                    if max_c >= C:
                        break  # 超出右边界，后续更长的 step_right 也必然越界

                    # 剩余需要向左退走的步数
                    step_left = (L - 1) - step_right
                    # 向左退走到的最终列
                    final_c = max_c - step_left
                    if final_c < 0 or final_c >= C:
                        continue  # 超出左边界

                    # 验证这条路径是否匹配单词 word
                    match = True
                    # 先向右走 step_right 步 (对应字符索引 0 到 step_right)
                    for i in range(step_right + 1):
                        if get_char(r, c + i) != word[i]:
                            match = False
                            break

                    if not match:
                        continue

                    # 再向左退走 step_left 步 (对应字符索引 step_right + 1 到 L - 1)
                    for j in range(1, step_left + 1):
                        if get_char(r, max_c - j) != word[step_right + j]:
                            match = False
                            break

                    if match:
                        total_count += 1

                # ----------------------------------------------------
                # 2. 垂直方向搜索 (起始必须是下 -> 允许折返向上)
                # ----------------------------------------------------
                # 枚举向下走的步数 step_down (从 0 到 L-1)
                for step_down in range(L):
                    # 向下到达的最远行
                    max_r = r + step_down
                    if max_r >= R:
                        break  # 超出下边界

                    # 剩余需要向上退走的步数
                    step_up = (L - 1) - step_down
                    # 向上退走到的最终行
                    final_r = max_r - step_up
                    if final_r < 0 or final_r >= R:
                        continue  # 超出上边界

                    # 验证这条路径是否匹配单词 word
                    match = True
                    # 先向下走 step_down 步
                    for i in range(step_down + 1):
                        if get_char(r + i, c) != word[i]:
                            match = False
                            break

                    if not match:
                        continue

                    # 再向上退走 step_up 步
                    for j in range(1, step_up + 1):
                        if get_char(max_r - j, c) != word[step_down + j]:
                            match = False
                            break

                    if match:
                        total_count += 1

    return total_count