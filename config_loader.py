import os
from pathlib import Path

import yaml

CONFIG_FILE = Path(__file__).parent / "config" / "config.yaml"


def load_config():
     # 1. 读环境变量，没设就默认 test
    env = os.environ.get("ENV", "test")

    # 2. 读配置文件
    with open(CONFIG_FILE, encoding="utf-8") as f:
        configs = yaml.safe_load(f)

    # 3. 检查环境名是否存在
    if env not in configs:
        raise ValueError(f"未知环境 {env}，可选：{list(configs.keys())}")

    # 4. 返回对应配置
    return configs[env]