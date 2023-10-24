def serialize_todo(todo):
    return {
        "id": todo.id,
        "created_at": todo.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": todo.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        "title": todo.title,
        "description": todo.description,
        "user_id": todo.user_id,
    }
