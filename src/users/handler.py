from src.users.service import list_users


def get_users_handler(request):
    return {"items": list_users()}