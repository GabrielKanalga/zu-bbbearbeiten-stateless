import helper
import pytest


@pytest.fixture
def setUp():
    helper.clear()


def test_add(setUp):
    assert len(helper.get_all()) == 0
    helper.add("test")
    assert len(helper.get_all()) == 1
    assert helper.get(0).text == "test"


def test_update(setUp):
    helper.add("test")
    assert not helper.get(0).isCompleted
    helper.update(0)
    assert helper.get(0).isCompleted
    helper.update(0)
    assert not helper.get(0).isCompleted


def test_bbbization(setUp):
    helper.add("Baden")
    assert helper.get(-1).text == "Bbbaden"
    helper.add("baden")
    assert helper.get(-1).text == "bbbaden"
