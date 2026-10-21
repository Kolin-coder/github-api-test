import requests

from config_loader import load_config

CONFIG = load_config()
BASE = CONFIG["base_url"]
TIMEOUT = CONFIG["timeout"]


def api_get(path, token=None, params=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return requests.get(BASE + path, headers=headers, params=params, timeout=TIMEOUT)







# import requests

# BASE = "https://api.github.com"

# def api_get(path, token=None, params=None):
#     """统一发 GET 请求"""
#     headers = {}
#     if token:
#         headers["Authorization"] = f"Bearer {token}"

#     return requests.get(BASE + path, headers=headers, params=params, timeout=10)