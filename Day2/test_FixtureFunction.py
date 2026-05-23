import pytest 

@pytest.fixture()
def setup():
    print("Launching the Browser")
    yield
    print("Closing the Browser")

class TestClass:
    def test_Login(self, setup):
        print("This is Login Test")

    def test_Search(self, setup):
        print("This is search Test")
