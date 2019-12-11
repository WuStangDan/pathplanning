import numpy as np
import matplotlib.pyplot as plt
start = np.array([842, 160])
goal = np.array([95, 518])
#start = np.array([1054, 721])
#goal = np.array([21, 453])
grid = np.load('new_york.npy')

# Copies of grid to be used for visualizing results.
path = np.zeros([len(grid), len(grid[0])], dtype=float)
# Make path results stand out more in figure.
path -= 1000
best_path = np.zeros([len(grid), len(grid[0])], dtype=int)


class AStarSearch:
    def __init__(self, start, goal, grid, path):
        self.pos = start
        self.pos_str = str(start)
        self.pos_depth = 0
        self.goal_str = str(goal)
        self.explored = {}
        self.not_explored = {}
        self.not_explored[str(start)] = 0
        self.grid = grid
        self.path = path

    # START - Student Section

    def get_possible_moves(self):
        # Get Potential Moves
        
        # For each potential move:
        #   -Check if each potential move is valid.
        #   -Check if move has already been explored.
        #   -Add to not explored list if valid and not explored.

        # Since all next possible moves have been determined,
        # consider current location explored.

        return True

    def goal_found(self):
        if True:
            # Add goal to path.
            return True
        return False

    def explore_next_move(self):
        # Determine next move to explore.

        # Determine the pos and depth of next move.
 
        # Write depth of next move onto path.
        self.path[self.pos[0], self.pos[1]] = round(0.0, 1)
        return True

    def heuristic(self, move):
        answer = 0.0
        return round(answer, 1)

    # END - Student Section

    # Helper Functions

    def generate_potential_moves(self, pos):
        u = np.array([-1, 0])
        d = np.array([1, 0])
        l = np.array([0, -1])
        r = np.array([0, 1])

        potential_moves = [pos + u, pos + d, pos + l, pos + r]
        # Students, uncomment the line below,  what happens?
        potential_moves += [pos + u+r, pos + u+l, pos + d+r, pos + d+l]
        return potential_moves

    def valid_move(self, move):
        # Check if out of boundary.
        if (move[0] < 0) or (move[0] >= len(grid)):
            return False
        if (move[1] < 0) or (move[1] >= len(grid[0])):
            return False
        # Check if wall or obstacle exists.
        if self.grid[move[0], move[1], 0] < 0.2:
            return False
        return True

    def string_to_array(self, string):
        string = string.replace('[', '')
        string = string.replace(']', '')
        string = string.split()
        array = [int(string[0]), int(string[1])]
        return np.array(array)


# Init
astar = AStarSearch(start, goal, grid, path)

explored_count = 0
while True:
    # Determine next possible moves.
    astar.get_possible_moves()
    if astar.goal_found():
        break
    astar.explore_next_move()
    # Print Progress Indicator
    if explored_count % 1000 == 0:
        print("Explored Count: " + str(explored_count))
    explored_count += 1


print('')
print('Fully explored count ' + str(len(path[path > 0])))

plt.imshow(path, cmap='jet', alpha=0.75)
plt.tight_layout()
plt.show()

pos = goal
goal_count = 0
while True:
    best_path[pos[0], pos[1]] = 1
    h_pos = round(path[pos[0], pos[1]], 1)
    if h_pos == 1:
        break
    potential_moves = astar.generate_potential_moves(pos)
    for move in potential_moves:
        if not astar.valid_move(move):
            continue
        h_move = path[move[0], move[1]]
        if h_move == (h_pos - 1):
            goal_count += 1
            pos = move
            break

print('Moves To Goal: ' + str(goal_count))
plt.imshow(grid, cmap='Greys')
plt.imshow(best_path, cmap='jet', alpha=0.75)
plt.tight_layout()
plt.show()
