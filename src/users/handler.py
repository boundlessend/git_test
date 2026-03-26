from src.users.service import list_users

ALLOWED_STATUSES = {"active", "blocked", "pending"}


def get_users_handler(request):
    status = request.get("query", {}).get("status")

    if status is not None:
        status = status.strip().lower()

        if status not in ALLOWED_STATUSES:
            return {"error": "invalid status", "code": 400}

    return {"items": list_users(status=status)}