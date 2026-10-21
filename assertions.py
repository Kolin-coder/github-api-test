def assert_status(resp, expected=200, label=""):
    """断言 HTTP 状态码"""
    prefix = f"{label}：" if label else ""

    assert resp.status_code == expected,f"{prefix}状态码不对，期望 {expected}，实际 {resp.status_code}，URL: {resp.url}"

def assert_is_list(resp, expected_count=None, label=""):
    """断言响应体是列表，可选断言元素个数"""
    prefix = f"{label}：" if label else ""

    data = resp.json()

    assert isinstance(data,list), f"{prefix}响应不是列表，实际是 {type(data).__name__}"

    if expected_count is not None:
        assert len(data) == expected_count, f"{prefix}条数不对，期望 {expected_count}，实际 {len(data)}"

    return data
