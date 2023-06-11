# 強化学習サンプル　ー月面着陸ー
# https://note.com/kikaben/n/n57584c49d5c2#a62d6edb-1aff-413d-ab81-5c5df2e01b36
#
import numpy as np
import gymnasium as gym
from gymnasium.envs.registration import register
import custom_env
from keymonitor import keymonitor, stop_keymonitor, get_command, is_pause, reset_command
import csv
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

gym.pprint_registry()

#env = gym.make("LunarLander-v2", render_mode="human")
#env = gym.make("AhonokoTank-v0", render_mode="human")
env = gym.make("mytaxi-v0", render_mode="human")

# Qテーブルの初期化
q_table = np.zeros((500, 6))

def update_q_table(_q_table, _action,  _observation, _next_observation, _reward, _episode):

    alpha = 0.2 # 学習率
    gamma = 0.99 # 時間割引き率

    # 行動後の状態で得られる最大行動価値 Q(s',a')
    next_max_q_value = max(_q_table[_next_observation])

    # 行動前の状態の行動価値 Q(s,a)
    q_value = _q_table[_observation][_action]

    # 行動価値関数の更新
    _q_table[_observation][_action] = q_value + alpha * (_reward + gamma * next_max_q_value - q_value)

    return _q_table

def get_action(_env, _q_table, _observation, _episode):
    epsilon = 0.002
    if np.random.uniform(0, 1) > epsilon:
        _action = np.argmax(_q_table[observation])
    else:
        _action = np.random.choice([0, 1, 2, 3, 4, 5])
    return _action

def save_data():
    global q_table
    with open('./q_table.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(q_table)
    f.close()

def menu(_commandkey):
    global done
    if _commandkey == 's':
        save_data()
        env.save_p()
    if _commandkey == 'q':
        done = True
        stop_keymonitor()
    reset_command()


def loop():

    global env, q_table, observation, done

    # ゲーム環境を初期化
    observation, info = env.reset()
    rewards = []
    done = False


    # 10000エピソードで学習する
    # ゲームのステップを1000回プレイ
    for episode in range(10000):

        if done:
            break

        total_reward = 0
        observation, info = env.reset()

        for turn in range(1000):

            if done:
                break

            if is_pause():
                menu(get_command())

            # 環境からランダムな行動を取得
            # これがエージェントの行動になるので、本来はAIが行動を決定するべきところ
    #       action = env.action_space.sample()
            action = get_action(env, q_table, observation, episode)

            # 行動を実行すると、環境の状態が更新される
    #        return (int(s), r, t, False, {"prob": p, "action_mask": self.action_mask(s)})
            next_observation, reward, terminated, truncated, info = env.step(action)
            if action == 4 or action == 5:
                print(action, observation, next_observation)

            # Qテーブルの更新
            q_table = update_q_table(q_table, action, observation, next_observation, reward, episode)
            total_reward += reward

            observation = next_observation

            if turn%10 == 0:
                print('episode: {}, turn:{}, total_reward: {}'.format(episode, turn, total_reward))

            # ゲームが終了したら、環境を初期化して再開
            if terminated or truncated:
                print('=================================')
                rewards.append(total_reward)
                break

    env.close()

if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(loop)
        executor.submit(keymonitor)


