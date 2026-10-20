"""
第 4 步 · 参数化：一份代码跑多组数据

注意文件名：必须以 test_ 开头，pytest 才会自动找到它。

这一步把你脑子里的用例表，直接变成代码。
"""

import pytest
import requests
from api_client import api_get

# 这张表就是你平时写用例时的那张表：
# 左边是输入，右边是预期结果
@pytest.mark.parametrize("username, expected_status", [
    ("torvalds", 200),                              # 正常用户
    ("Kolin-coder", 200),                           # 正常用户
    ("this-user-should-not-exist-12345", 404),      # 不存在的用户
])
def test_user_status(username, expected_status):
    """查用户接口：不同输入，对应不同预期状态码"""
    resp = api_get(f"/users/{username}")

    assert resp.status_code == expected_status, (
        f"用户 {username}：期望 {expected_status}，实际 {resp.status_code}"
    )
