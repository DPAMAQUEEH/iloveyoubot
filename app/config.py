from environs import Env

env = Env()
env.read_env()
TOKENTGAPI=env.str("BOT_TOKEN")