USERS = [
    {"id": 1, "email": "ivan@example.com", "status": "active"},
    {"id": 2, "email": "anna@example.com", "status": "blocked"},
    {"id": 3, "email": "petr@example.com", "status": "pending"},
    {"id": 4, "email": "olga@example.com", "status": "active"},
    {"id": 5, "email": "max@example.com", "status": "blocked"},
]


def get_all_users(status=None, sort=None):
    items = USERS

    if status is not None:
        items = [user for user in items if user["status"] == status]

    if sort == "email":
        items = sorted(items, key=lambda user: user["email"])

    return items