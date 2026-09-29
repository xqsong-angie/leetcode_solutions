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
    infected=set()
    def bfs(x,y):
        for dr in DIRECTIONS_8:
            dx=dr[0]
            dy=dr[1]
            if 0<=x+dx<rows and 0<=y+dy<cols and grid[x+dx][y+dy]==".":
                infected.add((x+dx,y+dy))
                
    days=0
    while True:
        for x,y in queue:
            if grid[x][y]=="X":
                bfs(x,y)
        for x,y in list(infected):
            grid[x][y]="X"
        days+=1
        if not infected:
            break
        infected=set()
    return days


# =====================================================================
# Part 2: Infection with Immune Obstacles
# =====================================================================
def min_days_to_stabilize_p2(grid: List[List[str]]) -> int:
    """
    Part 2: Calculates days until infection spread reaches equilibrium.
    '.' = Healthy, 'X' = Infected, 'I' = Immune (Obstacle)
    """
    # TODO: Implement Multi-source BFS treating 'I' as blocked cells
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    
    # Track initial infected cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                queue.append((r, c)) 
    
    infected=set()
    def bfs(x,y):
        for dr in DIRECTIONS_8:
            dx=dr[0]
            dy=dr[1]
            if 0<=x+dx<rows and 0<=y+dy<cols and grid[x+dx][y+dy]==".":
                infected.add((x+dx,y+dy))
                
    days=0
    while True:
        for x,y in queue:#🔥之后不要再用queue，没有update过
            if grid[x][y]=="X":
                bfs(x,y)
        for x,y in list(infected):
            grid[x][y]="X"
        days+=1
        if not infected:
            break
        infected=set()
    return days


# =====================================================================
# Part 3A: Infection with Recovery (Lifespan = D days)
# =====================================================================
def min_days_until_extinction_p3a(grid: List[List[str]], D: int) -> int:
    """
    Part 3A: Infected cells recover to 'I' after D days.
    Returns days until 0 active infected cells remain.
    """
    # TODO: Implement simulation tracking infection age or recovery queue
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    all_infected={}
    # Track initial infected cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                queue.append((r, c))
                all_infected[(r,c)]=0

    
    infected=set()
    def bfs(x,y):
        for dr in DIRECTIONS_8:
            dx=dr[0]
            dy=dr[1]
            if 0<=x+dx<rows and 0<=y+dy<cols and grid[x+dx][y+dy]==".":
                infected.add((x+dx,y+dy))
                all_infected[(x+dx,y+dy)]=0
                
    days=0
    while True:
        for k,v in all_infected:
            v+=1
            if v==D:
                all_infected.pop(k) #🔥永远不要在for循环内删除数据结构的东西！
                grid[k[0]][k[1]]=="I"
        for x,y in queue:
            if grid[x][y]=="X":
                bfs(x,y)
        for x,y in list(infected):
            grid[x][y]="X"
        days+=1
        if not infected and not all_infected:
            break
        infected=set()

    return days


# =====================================================================
# Part 3B: Threshold Infection (Requires >= T infected neighbors)
# =====================================================================
def min_days_to_stabilize_p3b(grid: List[List[str]], T: int) -> int:
    """
    Part 3B: Healthy cell infects only if infected_neighbors >= T.
    """
    # TODO: Maintain infected neighbor counts or step-by-step simulation
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    
    # Track initial infected cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                queue.append((r, c))
            else:
                grid[r][c]==0
    
    # TODO: Implement Multi-source BFS logic
    infected=set()
    def bfs(x,y):
        for dr in DIRECTIONS_8:
            dx=dr[0]
            dy=dr[1]
            if 0<=x+dx<rows and 0<=y+dy<cols and grid[r][c].isdigit():
                if grid[x+dx][y+dy]>=T:
                    infected.add((x+dx,y+dy))
                else:
                    grid[x+dx][y+dy]+=1
                
    days=0
    while True:
        for x,y in queue:
            if grid[x][y]=="X":
                bfs(x,y)
        for x,y in list(infected):
            grid[x][y]="X"
        days+=1
        if not infected:
            break
        infected=set()
    return days

# =====================================================================
# Part 4: Death Countdown Variant
# =====================================================================
def death_count_p4(grid: List[List[str]], K: int, C: int) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    
    # Track initial infected cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                queue.append((r, c))
                all_infected[(r,c)]=0
            else:
                grid[r][c]==C
    
    # TODO: Implement Multi-source BFS logic
    infected=set()
    all_infected={}
    def bfs(x,y):
        for dr in DIRECTIONS_8:
            dx=dr[0]
            dy=dr[1]
            if 0<=x+dx<rows and 0<=y+dy<cols and grid[r][c].isdigit():
                if grid[x+dx][y+dy]>=K:
                    infected.add((x+dx,y+dy))
                    all_infected[(x+dx,y+dy)]=0
                else:
                    grid[x+dx][y+dy]+=1
                
    days=0
    while True:
        for k,v in all_infected:
            if v>0:
                v-=1
            else:
                all_infected.pop(k)
                grid[k[0]][k[1]]=="I"
        for x,y in queue:
            if grid[x][y]=="X":
                bfs(x,y)
        for x,y in list(infected):
            grid[x][y]="X"
        days+=1
        if not infected and not all_infected:
            break
        infected=set()
    return days

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



#参考答案
from typing import List, Tuple
from collections import deque

DIRECTIONS_8 = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]


# =====================================================================
# Part 1: Basic Infection Simulation
# =====================================================================
def min_days_to_stabilize_p1(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                queue.append((r, c))
                
    days = 0
    while queue:
        newly_infected = []
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in DIRECTIONS_8:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.':
                    grid[nr][nc] = 'X'
                    newly_infected.append((nr, nc))
        
        if not newly_infected:
            break
        queue.extend(newly_infected)#🔥要更新
        days += 1

    return days


# =====================================================================
# Part 2: Infection with Immune Obstacles
# =====================================================================
def min_days_to_stabilize_p2(grid: List[List[str]]) -> int:
    # 'I' acts as an obstacle; healthy cells '.' get infected identically to Part 1
    return min_days_to_stabilize_p1(grid) #🔥同样解法直接引用函数即可，复制粘贴可能格式混乱


# =====================================================================
# Part 3A: Infection with Recovery (Lifespan = D days)
# =====================================================================
def min_days_until_extinction_p3a(grid: List[List[str]], D: int) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    # Store: (r, c, day_infected)
    active_infected = deque()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                active_infected.append((r, c, 0))
    
    day = 0
    while active_infected:
        day += 1
        # 1. Spread infection from currently active cells
        newly_infected = []
        for r, c, start_day in list(active_infected):
            for dr, dc in DIRECTIONS_8:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.':
                    grid[nr][nc] = 'X'
                    newly_infected.append((nr, nc, day))
        
        # 2. Recover cells that reached age D
        surviving_infected = deque()
        for r, c, start_day in active_infected:
            if day - start_day >= D:
                grid[r][c] = 'I'  # Recovered/Immune
            else:
                surviving_infected.append((r, c, start_day))
                
        active_infected = surviving_infected
        active_infected.extend(newly_infected)

    return day


# =====================================================================
# Part 3B: Threshold Infection (Requires >= T infected neighbors)
# =====================================================================
def min_days_to_stabilize_p3b(grid: List[List[str]], T: int) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    days = 0
    
    while True:
        to_infect = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    # Count adjacent infected neighbors
                    inf_count = 0
                    for dr, dc in DIRECTIONS_8:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 'X':
                            inf_count += 1
                    if inf_count >= T:
                        to_infect.append((r, c))
        
        if not to_infect:
            break
            
        for r, c in to_infect:
            grid[r][c] = 'X'
            
        days += 1

    return days


# =====================================================================
# Part 4: Death Countdown Variant
# =====================================================================
def death_count_p4(grid: List[List[str]], K: int, C: int) -> int:
    """
    Healthy cells with >= K infected neighbors enter a countdown C.
    After C consecutive days in countdown, they transition to 'dead' ('I').
    """
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    countdown = {} # Maps (r, c) -> remaining_days
    days = 0

    while True:
        next_countdown = {}
        changed = False
        
        # Evaluate healthy cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    inf_count = sum(
                        1 for dr, dc in DIRECTIONS_8
                        if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == 'X'
                    )
                    
                    if inf_count >= K:
                        # Continue or start countdown
                        rem_days = countdown.get((r, c), C) - 1
                        if rem_days == 0:
                            grid[r][c] = 'I'  # Dead/Obstacle
                            changed = True
                        else:
                            next_countdown[(r, c)] = rem_days
                            changed = True

        countdown = next_countdown
        days += 1
        
        if not changed:
            break

    return days