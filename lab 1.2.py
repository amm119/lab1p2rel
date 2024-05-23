import numpy as np

class GridWorld:

    def __init__(self):
        self.grid_size = (3, 3)
        # There are Up, Down, Left, Right actions
        self.num_actions = 4  # Define number of actions
        self.rewards = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0]  # Reward of +1 in the bottom-right cell
        ])

    def get_reward(self, state):
        # Extract the row and column from the state tuple
        row, col = state
        # Return the reward associated with the given state
        return self.rewards[row, col]

class ValueFunction:

    # Create values array with same size as grid and initialize all elements to zero
    def __init__(self, grid_size):
        self.values = np.zeros(grid_size)

    # Update value at specified state with new_value
    def update_value(self, state, new_value):
        row, col = state
        self.values[row, col] = new_value

    # Get value at specified state
    def get_value(self, state):
        row, col = state
        return self.values[row, col]
    
grid_world = GridWorld()
value_function = ValueFunction(grid_world.grid_size)

# Initialize the value function with the rewards associated with each cell
for i in range(grid_world.grid_size[0]):
    for j in range(grid_world.grid_size[1]):
        value_function.update_value((i, j), grid_world.get_reward((i, j)))

# Print the initial value function to see the value estimates for each state
print("Initial value function:")
print(value_function.values)