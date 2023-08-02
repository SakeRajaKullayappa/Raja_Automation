import pytest


@pytest.mark.smoke
def test_Login():
    print("Login was Done")


@pytest.mark.regression
def test_AddProduct():
    print("Product Adding was Done")


@pytest.mark.smoke
def test_Logout():
    print("Logout was Done")