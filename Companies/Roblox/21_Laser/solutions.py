def solution(
    numRows: int,
    numColumns: int,
    curRow: int,
    curColumn: int,
    laserCoordinates: list[list[int]],
) -> int:
    # 收集所有有激光的行和列（假设坐标从 0 开始；若题目为 1-based，下面直接匹配即可）
    bad_rows = {r for r, c in laserCoordinates}
    bad_cols = {c for r, c in laserCoordinates}

    # 四个方向：(row_change, col_change)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_safe_cells = 0

    for dr, dc in directions:
        safe_cells = 1  # 包含了起始格（起始格始终安全）
        r, c = curRow + dr, curColumn + dc

        # 沿着当前方向一直向前走
        while (
            0 <= r < numRows
            and 0 <= c < numColumns
            and r not in bad_rows
            and c not in bad_cols
        ):
            safe_cells += 1
            r += dr
            c += dc

        # 更新四个方向中的最大值
        max_safe_cells = max(max_safe_cells, safe_cells)

    return max_safe_cells