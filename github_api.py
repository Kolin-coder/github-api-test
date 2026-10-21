from api_client import api_get


def get_user(username):
    """查指定用户的信息（公开，不需要 token）"""
    # 返回 api_get(...)
    return api_get(f"/users/{username}")

def list_user_repos(username, per_page=30):
    """查指定用户的仓库列表"""
    # 返回 api_get(...)，注意 per_page 用 params 传
    resp=api_get(f"/users/{username}",params={"per_page":per_page})
    return resp

def get_my_profile(token):
    """查自己的信息（需要认证）"""
    # 返回 api_get("/user", token=token)
    resp=api_get(f"/users",token=token)

