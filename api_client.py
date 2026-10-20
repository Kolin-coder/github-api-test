import requests

BASE = "https://api.github.com"

def api_get(path, token=None, params=None):
    """统一发 GET 请求"""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    return requests.get(BASE + path, headers=headers, params=params, timeout=10)