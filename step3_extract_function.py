"""
第 3 步 · 抽函数：把「发请求」从「做断言」里拆出来

上一版里，请求怎么发、断言怎么断，混在同一个函数里。
接口一多，每个测试函数都要重复写 headers、timeout、URL 拼接。

这一步把它们拆开：
  api_get()     只负责发请求
  test_xxx()    只负责断言
"""

import os

import requests

BASE = "https://api.github.com"


def api_get(path, token=None):
    """统一发 GET 请求 —— 所有接口都走这里"""
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = BASE + path
    return requests.get(url, headers=headers, timeout=10)


def test_rate_limit():
    """测限流接口"""
    token = os.environ["GITHUB_TOKEN"]

    resp = api_get("/rate_limit", token=token)

    assert resp.status_code == 200, f"状态码不对，实际是 {resp.status_code}"

    core = resp.json()["resources"]["core"]
    assert core["limit"] == 5000, f"上限不对，实际是 {core['limit']}"
    assert core["remaining"] <= core["limit"], "剩余次数超过上限，数据异常"

    print("限流接口：3 条断言通过")


def test_user_info():
    """测用户接口 —— 顺便证明 api_get 能复用"""
    token = os.environ["GITHUB_TOKEN"]

    resp = api_get("/user", token=token)

    assert resp.status_code == 200, f"状态码不对，实际是 {resp.status_code}"

    data = resp.json()
    assert "login" in data, "返回里没有 login 字段"

    print(f"用户接口：通过，当前用户 {data['login']}")


if __name__ == "__main__":
    test_rate_limit()
    test_user_info()
