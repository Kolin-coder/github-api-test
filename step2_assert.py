"""
第 2 步 · 加断言：从「打印结果」变成「判断对错」

第 1 步的脚本只是把数字打印出来，对不对得你自己看。
这一步加上断言 —— 让程序自己判断，不符合预期就直接报错停下。
"""

import os

import requests

API = "https://api.github.com/rate_limit"


def test_rate_limit():
    """带 token 调用，断言返回符合预期"""

    token = os.environ["GITHUB_TOKEN"]

    resp = requests.get(
        API,
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )

    # 断言 1：状态码必须是 200
    assert resp.status_code == 200, f"状态码不对，实际是 {resp.status_code}"

    core = resp.json()["resources"]["core"]

    # 断言 2：认证后每小时上限必须是 5000
    assert core["limit"] == 5000, f"上限不对，实际是 {core['limit']}"

    # 断言 3：剩余次数不可能超过上限，超过就说明数据异常
    assert core["remaining"] <= core["limit"], "剩余次数超过上限，数据异常"

    print("3 条断言全部通过")


if __name__ == "__main__":
    test_rate_limit()
