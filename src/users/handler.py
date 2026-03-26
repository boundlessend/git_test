from src.users.service import list_users


def get_users_handler(request):
    status = request.get("query", {}).get("status")

    if status is not None:
        status = status.strip().lower()

    return {"items": list_users(status=status)}