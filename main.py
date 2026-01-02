import yfinance as yf
from agent import TradeAgent
import numpy as np

# 1. Download Real Market Data
data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")['Close'].values

# 2. Setup Agent
state_size = 5 # Look back at last 5 days
agent = TradeAgent(state_size, 3) # Actions: 0=Sell, 1=Hold, 2=Buy

# 3. Training Loop (Simplified)
print("Starting Training on AAPL Data...")
for episode in range(10):
    for t in range(len(data) - state_size - 1):
        state = data[t:t+state_size]
        action = agent.act(state)
        # (Simplified environment logic here)
    print(f"Episode {episode} Complete")
