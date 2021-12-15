import random
import pytest

@pytest.fixture
def gen_a_mobile():
    """随机生成 13 开头的手机号码。"""
    random_num = "".join([str(random.randint(1,9)) for i in range(9)])
    return "".join(["13", random_num])

def test_register(gen_a_mobile):
    assert "13333333333" == gen_a_mobile