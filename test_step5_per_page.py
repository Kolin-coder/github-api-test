from api_client import api_get

path="/users/microsoft/repos"


def test_per_page_over_limit():
    resp=api_get(path,params={"per_page":200})
    count=len(resp.json())
    assert resp.status_code == 200 , f"状态码不对，实际是 {resp.status_code}"

    assert count == 100, f"应该返回 100 条，实际 {count} 条"
    
