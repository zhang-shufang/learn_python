import pytest
from python_repos_vis import run_api

def test_run_api():
    """输入制定url，返回结果的.status_code属性等于200，则测试通过"""
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    r = run_api(url)
    assert r.status_code == 200