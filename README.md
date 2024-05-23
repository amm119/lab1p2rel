# REL_lab

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.x

## Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/NgDMTruc/REL_lab.git
    cd REL_lab
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```


## Running the Scripts

Each question corresponds to a specific command that needs to be run in the terminal. Below are the commands for each question:

### Q1

To run the value iteration algorithm with 100 iterations and 10 episodes:
```sh
python gridworld.py -a value -i 100 -k 10
```

or in short with 5 iterations
```
 python gridworld.py -a value -i 5
```

### Q2

BridgeGrid is a grid world map with the a low-reward terminal state and a high-reward terminal state separated by a narrow "bridge", on either side of which is a chasm of high negative reward. The agent starts near the low-reward state. With the default discount of 0.9 and the default noise of 0.2, the optimal policy does not cross the bridge. Change only ONE of the discount and noise parameters so that the optimal policy causes the agent to attempt to cross the bridge.

```sh
python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2
```
### Q3

Running value iteration on DiscountGrid with specified discount, noise, and living reward parameters

```sh
python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.2 --livingReward 0.0
```

