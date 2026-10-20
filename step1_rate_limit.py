"""
第 1 步 · 调一个接口，看看它返回什么

这个脚本只干一件事：分别用「不带 token」和「带 token」两种身份，
去问 GitHub 一句话 ——「我这个身份还能调多少次接口？」

对比两次的数字，你就明白 token 到底在干什么了。
"""

import os
import sys

import requests

# Windows 终端默认编码可能不是 UTF-8，这行保证中文不乱码
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# 要调的接口地址
API = "https://api.github.com/rate_limit"


def check_limit(token=None):
    """问 GitHub：我这个身份还能调多少次接口？"""

    # headers 是随请求一起发过去的附加信息
    headers = {}

    # 有 token 就带上 —— 这是你的「身份证明」
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # 发 GET 请求。timeout=10 表示 10 秒没响应就报错，别傻等
    resp = requests.get(API, headers=headers, timeout=10)

    # 200 表示成功
    print("状态码:", resp.status_code)

    # .json() 把返回的 JSON 文本变成 Python 字典
    data = resp.json()
    core = data["resources"]["core"]

    print("每小时上限:", core["limit"])
    print("当前剩余:", core["remaining"])
    print()


print("=" * 46)
print("① 匿名访问（不带 token）")
print("=" * 46)
check_limit()

token = os.environ.get("GITHUB_TOKEN")

print("=" * 46)
print("② 认证访问（带 token）")
print("=" * 46)

if not token:
    print("× 没读到环境变量 GITHUB_TOKEN")
    print()
    print("排查顺序：")
    print('  1. 是否执行过  setx GITHUB_TOKEN "ghp_你的token"')
    print("  2. 执行完是否重开了终端（VS Code 要整个重启）")
    print("  3. 在 PowerShell 里执行  $env:GITHUB_TOKEN  看看有没有值")
else:
    check_limit(token)
    print("token 已读取，长度", len(token), "位")
