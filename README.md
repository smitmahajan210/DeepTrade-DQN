# 📈 DeepTrade-DQN: PyTorch AI Trading Agent

An autonomous AI agent that uses **Deep Reinforcement Learning (DQN)** to navigate stock market volatility. Built with PyTorch and trained on real-time data from Yahoo Finance.

## 🏗️ Architecture
- **Framework**: PyTorch
- **Algorithm**: Deep Q-Learning (DQN) with Experience Replay
- **Data Source**: `yfinance` (Apple, Tesla, BTC)
- **Environment**: Custom Trading Simulation (Buy/Hold/Sell)

## 🛠️ Setup
1. Clone this repo.
2. Run `pip install -r requirements.txt`.
3. Run `python main.py` to start training the agent on historical AAPL data.

## 📊 Result
The agent learns to identify price trends and optimizes its "Reward" (Total Profit) while minimizing "Loss" (Drawdown).
