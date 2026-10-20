from api_client import api_get


def test_my_profile(token):
    """查自己的信息，需要认证"""
    resp = api_get("/user", token=token)

    assert resp.status_code == 200, f"状态码不对，实际是 {resp.status_code}"

    data = resp.json()
    assert data["login"] == "Kolin-coder", f"用户名不对，实际是 {data['login']}"
