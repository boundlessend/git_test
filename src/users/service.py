from src.users.repository import get_all_users


def list_users(status=None):
    return get_all_users(status=status)