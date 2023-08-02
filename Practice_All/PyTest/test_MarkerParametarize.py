import pytest


@pytest.mark.parametrize("uName, pwd",
                         [
                             ("Selenium", "Webdriver"),
                             ("Pytest", "Pycharm"),
                             ("Raja", "Sake")
                         ]

                         )
def test_Login(uName, pwd):
    print(uName)
    print(pwd)
