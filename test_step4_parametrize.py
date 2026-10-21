"""
第 4 步 · 参数化：一份代码跑多组数据

注意文件名：必须以 test_ 开头，pytest 才会自动找到它。

这一步把你脑子里的用例表，直接变成代码。
"""

import pytest
from pathlib import Path
import yaml

from github_api import get_user
from github_api import list_user_repos
from assertions import assert_status, assert_is_list


DATA_FILE = Path(__file__).parent / "data" / "user_cases.yaml"

def load_cases():
    with open(DATA_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)["user_status_cases"]

@pytest.mark.parametrize("case", load_cases(),ids=lambda c: f"{c['username']}-{c['expected_status']}",)
def test_user_status(case):
    resp = get_user(case["username"])
    assert_status(resp, case["expected_status"], case["desc"])

    
def load_repos_cases():
    with open (DATA_FILE,encoding="utf-8") as f:
        return yaml.safe_load(f)["repo_list_cases"]

@pytest.mark.parametrize("case",load_repos_cases(),ids=lambda c: f"{c['username']}-per{c['per_page']}")
def test_repos_list_count(case):
    resp = list_user_repos(case["username"], per_page=case["per_page"])
    assert_status(resp, 200, case["desc"])
    data = assert_is_list(resp, case["expected_count"], case["desc"])


# @pytest.mark.parametrize("case", load_cases(),ids=lambda c: f"{c['username']}-{c['expected_status']}",)
# def test_user_status(case):
#     resp=get_user(case["username"])
#     # assert case["expected_status"] == 200,f"用户{case["username"]}：实际{case["expected_status"]}"
#     assert resp.status_code == case["expected_status"], (
#     f"{case['desc']}：用户 {case['username']} "
#     f"期望 {case['expected_status']}，实际 {resp.status_code}"
# )

# def load_repos_cases():
#     with open (DATA_FILE,encoding="utf-8") as f:
#         return yaml.safe_load(f)["repo_list_cases"]

# @pytest.mark.parametrize("case",load_repos_cases(),ids=lambda c: c['desc'])
# def test_repos_list_count(case):
#     resp=list_user_repos(case["username"],per_page=case["per_page"])

#     assert resp.status_code == 200,f"{case['desc']}:状态码{resp.status_code}"

#     actual=len(resp.json())
#     assert actual ==case["expected_count"],f"{case['desc']}:期望为{case["expected_count"]},实际为{actual}"