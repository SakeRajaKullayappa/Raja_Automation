def test_1():
    x = 10
    y = 20
    assert x == y, "x and y are not same"


def test_2():
    x = 10
    y = 10
    assert x == y, "x and y are not same"


def test_3():
    name = "Raja"
    title = "Raja is Not a Bad Person"
    assert name in title, "name is not presented in title"


def test_4():
    tool = "Jenkins"
    title = "Jenkins is a CI/CD tool"
    assert tool in title, "tool does not matched in title"
