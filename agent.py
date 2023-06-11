# 強化学習サンプル　ー月面着陸ー
# https://note.com/kikaben/n/n57584c49d5c2#a62d6edb-1aff-413d-ab81-5c5df2e01b36
#
import gymnasium as gym
from gymnasium.envs.registration import register
import custom_env

#print("__init__.py loaded.")

#register(
#    id='AhonokoTank-v0',
#    entry_point='custom_env.envs:AhonokoTank'
#)
gym.pprint_registry()

# 月着陸(Lunar Lander)ゲームの環境を作成
#env = gym.make("LunarLander-v2", render_mode="human")
#env = gym.make("AhonokoTank-v0", render_mode="human")
env = gym.make("mytaxi-v0", render_mode="human")



# ゲーム環境を初期化
observation, info = env.reset()

# ゲームのステップを1000回プレイ
for _ in range(5000):
    # 環境からランダムな行動を取得
    # これがエージェントの行動になるので、本来はAIが行動を決定するべきところ
    action = env.action_space.sample()

    # 行動を実行すると、環境の状態が更新される
    observation, reward, terminated, truncated, info = env.step(action)

    # ゲームが終了したら、環境を初期化して再開
    if terminated or truncated:
        observation, info = env.reset()

env.close()
