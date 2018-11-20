import pytest
from collections import namedtuple
from workspace.config.running_config import get_driver

@pytest.fixture(scope='function')
def driver():
    d = get_driver()
    return d


@pytest.fixture(scope='function')
def login_data():
    '''
    返回数据用于测试登录
    '''
    LoginData = namedtuple('LoginData', 'casename username password asserts')
    return (
        LoginData("用户名为空", '', 'password', '账号不能为空！'),
        LoginData("密码为空", 'admin', '', '密码不能为空！'),
        LoginData("本地登录", 'admin', '1234567890', '系统管理员'),
        LoginData("AD登录", 'wjx', 'Admin123', 'weijiaxin有一个超级长的名字')
    )