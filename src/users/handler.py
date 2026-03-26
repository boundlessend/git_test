from src.users.service import list_users

ALLOWED_STATUSES = {"active", "blocked", "pending"}
ALLOWED_SORTS = {"email"}


def get_users_handler(request):
    query = request.get("query", {})
    status = query.get("status")
    sort = query.get("sort")

    if status is not None:
        status = status.strip().lower()

        if status not in ALLOWED_STATUSES:
            return {"error": "invalid status", "code": 400}

    if sort is not None:
        sort = sort.strip().lower()

        if sort not in ALLOWED_SORTS:
            return {"error": "invalid sort", "code": 400}

    return {"items": list_users(status=status, sort=sort)}