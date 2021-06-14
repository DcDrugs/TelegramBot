import pytest
import uuid
from ugc.models import Profiler, Item


@pytest.fixture
def user_data():
    return {"external_id": 646366, "name": "pasha1234567890"}

test=uuid.uuid4()

@pytest.fixture
def item_data():
    return {"id": test, "cost": 50, "name": "Iphone"}


@pytest.fixture
def user_bd():
    return Profiler.objects.create(external_id=646366, name="pasha1234567890")


@pytest.fixture
def item_bd(user_bd):
    return Item.objects.create(profiler=user_bd, id=test, name="Iphone", cost=50)


def check(d: dict, item):
    for key, value in d.items():
        assert getattr(item, key) == value


@pytest.mark.django_db
def test_user_type(user_data, user_bd):
    check(user_data, user_bd)


@pytest.mark.django_db
def test_item_type(item_data, item_bd):
    check(item_data, item_bd)
