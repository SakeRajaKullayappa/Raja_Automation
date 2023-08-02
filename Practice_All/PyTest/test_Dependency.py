import pytest


class Test_Dependency:

    @pytest.mark.dependency()
    def test_Method1(self):
        print("Method 1 Execution")
        assert 1 + 2 == 4, "Assert Got Failed"

    @pytest.mark.dependency(depends=["Test_Dependency::test_Method1"])
    def test_Method2(self):
        print("Method 2 Execution")

    def test_Method3(self):
        print("Method 3 Execution")
