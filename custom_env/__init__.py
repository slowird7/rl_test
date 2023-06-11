from gymnasium.envs.registration import register

print("__init__.py loaded.")

register(
    id='AhonokoTank-v0',
    entry_point='custom_env.envs.Ahonoko_Tank:AhonokoTank'
)

register(
    id='mytaxi-v0',
    entry_point='custom_env.envs.mytaxi:TaxiEnv'
)

register(
    id='mymountaincar-v0',
    entry_point='custom_env.envs.mountain_car:MountainCarEnv'
)
