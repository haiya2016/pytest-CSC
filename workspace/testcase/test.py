import pytest


@pytest.mark.parametrize('name, l, s',
                         [
                            ('failed', [1, 2, 3], 4),
                            ('pass', [1, 3], 4),
                            ('failed01', [1, '2', 3], 4),
                            ('failed02', [1, 2, 3], '4'),
                            ('failed03', '[1, 2, 3]', 4)
                         ]
                        )
def test_fun(name, l, s):
    assert sum(l) == s


if __name__ == "__main__":
    pytest.main(['./workspace/testcase/test.py'])