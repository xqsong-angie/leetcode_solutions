from typing import List, Tuple
from collections import deque
import copy

# 8-directional neighbor offsets (up, down, left, right + 4 diagonals)
DIRECTIONS_8 = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]


# =====================================================================
# Part 1: Basic Infection Simulation
# =====================================================================
def min_days_to_stabilize_p1(grid: List[List[str]]) -> int:
    """
    Part 1: Calculates days until infection spread reaches equilibrium.
    '.' = Healthy, 'X' = Infected
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    
    # Track initial infected cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                queue.append((r, c))
    
    # TODO: Implement Multi-source BFS logic
    return 0


# =====================================================================
# Part 2: Infection with Immune Obstacles
# =====================================================================
def min_days_to_stabilize_p2(grid: List[List[str]]) -> int:
    """
    Part 2: Calculates days until infection spread reaches equilibrium.
    '.' = Healthy, 'X' = Infected, 'I' = Immune (Obstacle)
    """
    # TODO: Implement Multi-source BFS treating 'I' as blocked cells
    return 0


# =====================================================================
# Part 3A: Infection with Recovery (Lifespan = D days)
# =====================================================================
def min_days_until_extinction_p3a(grid: List[List[str]], D: int) -> int:
    """
    Part 3A: Infected cells recover to 'I' after D days.
    Returns days until 0 active infected cells remain.
    """
    # TODO: Implement simulation tracking infection age or recovery queue
    return 0


# =====================================================================
# Part 3B: Threshold Infection (Requires >= T infected neighbors)
# =====================================================================
def min_days_to_stabilize_p3b(grid: List[List[str]], T: int) -> int:
    """
    Part 3B: Healthy cell infects only if infected_neighbors >= T.
    """
    # TODO: Maintain infected neighbor counts or step-by-step simulation
    return 0


# =====================================================================
# Test Runner & Unit Tests
# =====================================================================
def run_all_tests():
    print("--- Running Infection Simulation Tests ---")
    
    # -----------------------------------------------------------------
    # Test Part 1
    # -----------------------------------------------------------------
    grid_p1_1 = [
        [".", ".", "."],
        [".", "X", "."],
        [".", ".", "."]
    ]
    # Center spreads to all 8 neighbors on Day 1 -> Stable on Day 1
    assert min_days_to_stabilize_p1(grid_p1_1) == 1, "P1 Test 1 Failed"
    
    grid_p1_empty = []
    assert min_days_to_stabilize_p1(grid_p1_empty) == 0, "P1 Edge Case Failed"
    
    print("✓ Part 1 Tests Passed!")

    # -----------------------------------------------------------------
    # Test Part 2
    # -----------------------------------------------------------------
    grid_p2_1 = [
        ["X", "I", "."],
        ["I", "I", "."],
        [".", ".", "."]
    ]
    # Blocked by 'I', cannot spread anywhere -> Stable on Day 0
    assert min_days_to_stabilize_p2(grid_p2_1) == 0, "P2 Test 1 Failed"
    
    print("✓ Part 2 Tests Passed!")

    # -----------------------------------------------------------------
    # Test Part 3A
    # -----------------------------------------------------------------
    grid_p3a = [
        ["X", ".", "."]
    ]
    # D=1: Day 0 (X, ., .), Day 1 infects next cell but original recovers -> (I, X, .) -> Day 2 (I, I, X) -> Day 3 (I, I, I) -> Extinct at Day 3
    # assert min_days_until_extinction_p3a(grid_p3a, 1) == 3
    
    print("✓ All runnable tests passed successfully!")

if __name__ == "__main__":
    run_all_tests()