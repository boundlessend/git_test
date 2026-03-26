USERS = [
    {"id": 1, "email": "ivan@example.com", "status": "active", "is_deleted": False},
    {"id": 2, "email": "anna@example.com", "status": "blocked", "is_deleted": False},
    {"id": 3, "email": "petr@example.com", "status": "pending", "is_deleted": False},
    {"id": 4, "email": "olga@example.com", "status": "active", "is_deleted": False},
    {"id": 5, "email": "max@example.com", "status": "blocked", "is_deleted": True},
]


def get_all_users(status=None):
    if status is None:
        return USERS

    return [user for user in USERS if user["status"] == status]