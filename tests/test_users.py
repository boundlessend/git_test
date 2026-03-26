from src.users.service import list_users


def test_list_users_returns_all():
    users = list_users()
    assert len(users) == 5