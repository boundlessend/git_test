from src.users.service import list_users
from src.users.handler import get_users_handler


def test_list_users_returns_all():
    users = list_users()
    assert len(users) == 5


def test_list_users_returns_only_active():
    users = list_users(status="active")
    assert len(users) == 2
    assert [user["id"] for user in users] == [1, 4]


def test_list_users_returns_only_blocked():
    users = list_users(status="blocked")
    assert len(users) == 2
    assert [user["id"] for user in users] == [2, 5]


def test_get_users_handler_returns_400_for_invalid_status():
    response = get_users_handler({"query": {"status": "archived"}})
    assert response["code"] == 400
    assert response["error"] == "invalid status"