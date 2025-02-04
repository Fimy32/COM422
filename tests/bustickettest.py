import pytest
import Week3.busticket

@pytest.fixture
def young_age():
    age = 3

def test_toddler_ticket(young_age):
    assert (Week3.busticket.buy_ticket())
