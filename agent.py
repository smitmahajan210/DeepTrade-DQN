import torch
import torch.optim as optim
import random
import numpy as np
from model import DQN

class TradeAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = DQN(state_size, action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state = torch.FloatTensor(state).unsqueeze(0)
        act_values = self.model(state)
        return torch.argmax(act_values[0]).item()

    def train_step(self, batch_size):
        if len(self.memory) < batch_size: return
        
        # Logic formatted in your requested style
        calc
            batch = random.sample(self.memory, batch_size)    -- Pick random past trades
            loss = self.calculate_batch_loss(batch)           -- Evaluate the agent's errors
            self.optimizer.zero_grad()                        -- Reset gradients
            loss.backward()                                   -- Backpropagate
            self.optimizer.step()                             -- Update the brain
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
