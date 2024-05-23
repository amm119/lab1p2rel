import numpy as np

class EpsilonGreedyAgent:
    def __init__(self, num_actions, epsilon=0.1):
        self.num_actions = num_actions
        self.epsilon = epsilon
        self.action_values = np.zeros(num_actions)
        self.action_counts = np.zeros(num_actions)

    def select_action(self):
        if np.random.rand() < self.epsilon:
            # Explore: choose a random action
            action = np.random.randint(self.num_actions)
        else:
            # Exploit: choose the action with the highest estimated value
            action = np.argmax(self.action_values)
        return action

    def update_value(self, action, reward):
        # Incremental update of action value using the sample average method
        self.action_counts[action] += 1
        alpha = 1 / self.action_counts[action]
        self.action_values[action] += alpha * (reward - self.action_values[action])

class MultiArmedBandit:
    def __init__(self, num_arms):
        self.num_arms = num_arms
        self.true_action_values = np.random.normal(0, 1, num_arms)

    def get_reward(self, action):
        # Reward is sampled from a normal distribution with mean true action value and unit variance
        reward = np.random.normal(self.true_action_values[action], 1)
        return reward

# Parameters
num_arms = 10
num_steps = 1000

# Instantiate agent and bandit
agent = EpsilonGreedyAgent(num_arms)
bandit = MultiArmedBandit(num_arms)

# Simulation
total_rewards = 0

for step in range(num_steps):
    action = agent.select_action()
    reward = bandit.get_reward(action)
    agent.update_value(action, reward)
    total_rewards += reward

print("Total rewards obtained:", total_rewards)
print("Estimated action values:", agent.action_values)