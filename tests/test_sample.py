def sum_off(a, b):
    return a + b


def test_url_shortener():
    a = 10
    b = 20
    result = sum_off(a, b)
    import os
    print(os.getenv("abcd"))
    print(os.getenv("cd"))
    assert result == 30
    assert os.getenv("abcd") == 1234
