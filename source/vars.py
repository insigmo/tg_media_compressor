import os
from pathlib import Path

from environs import Env

root_path = Path('.').parent
config_path = Path(root_path) / 'build/dev.env'
env = Env()
env.read_env(str(config_path))


class Vars:
    root_dir = root_path
    bot_token = os.environ['BOT_TOKEN']
