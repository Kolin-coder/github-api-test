import os

import pytest


@pytest.fixture
def token():
    """从环境变量取 GitHub token"""
    return os.environ["GITHUB_TOKEN"]