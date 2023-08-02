import sys

import pytest


@pytest.mark.skip
def test_Login():
    print("Login was Done")


@pytest.mark.skipif(sys.version_info < (3, 12), reason='Python Version is Not Supported')
def test_AddProduct():
    print("Product Adding was Done")


@pytest.mark.xfail
def test_Logout():
    assert True
    print("Logout was Done")


@pytest.mark.xpass
def test_CloseApplication():
    assert True
    print("Closing the Application was Done")