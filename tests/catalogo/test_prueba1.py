import pytest

@pytest.mark.marca1
def test_prueba():
    assert 1 == 1

@pytest.mark.marca1
def test_prueba2():
    assert  2 == 1

@pytest.fixture(scope="session")
def fixture_1():
    print("Desde el fixture")
    yield 1

@pytest.mark.marca1
def test_prueba3(fixture_1):
    print("Desde el test")
    variable = fixture_1
    assert variable== 1