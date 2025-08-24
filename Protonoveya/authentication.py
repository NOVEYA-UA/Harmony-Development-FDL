import json

def authenticate_user(input_phrase):
    with open("users.json", "r") as file:
        users = json.load(file)["users"]

    for user in users:
        if user["name"] in input_phrase:
            return f"Доступ разрешён: {user['role']}"

    return "Ошибка: пользователь не найден."

# Пример вызова
print(authenticate_user("Я, Татьяна Бондаренко, участник проекта НОВЕЯ."))
