def serialize_todo(todo):
    return {
        "id": todo.id,
        "created_at": todo.created_at,
        "updated_at": todo.updated_at,
        "title": todo.title,
        "description": todo.description,
        "user_id": todo.user_id,
    }
