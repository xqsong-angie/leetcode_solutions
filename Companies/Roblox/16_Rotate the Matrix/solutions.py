def solution(matrix, turns):
    n = len(matrix)
    effective_turns = turns % 4
    
    # If 0 turns required, return original matrix copy
    if effective_turns == 0:
        return [row[:] for row in matrix]
    
    # Perform effective_turns times clockwise rotation of the 4 regions
    result = [row[:] for row in matrix]
    
    for _ in range(effective_turns):
        curr = [row[:] for row in result]
        for r in range(n):
            for c in range(n):
                # Check if element is on either diagonal
                if r == c or r + c == n - 1:
                    continue  # Diagonals stay unchanged
                
                # Determine which region the cell (r, c) belongs to and map to its new rotated position
                if r < c and r + c < n - 1:
                    # Top region -> Right region: (r, c) becomes (c, n - 1 - r)
                    result[c][n - 1 - r] = curr[r][c]
                elif r < c and r + c > n - 1:
                    # Right region -> Bottom region: (r, c) becomes (c, n - 1 - r)
                    result[c][n - 1 - r] = curr[r][c]
                elif r > c and r + c > n - 1:
                    # Bottom region -> Left region: (r, c) becomes (c, n - 1 - r)
                    result[c][n - 1 - r] = curr[r][c]
                elif r > c and r + c < n - 1:
                    # Left region -> Top region: (r, c) becomes (c, n - 1 - r)
                    result[c][n - 1 - r] = curr[r][c]

    return result