from db_config import Message


# ユーザー追加
def add_user(name, age):
    Message.create(name=name, age=age)


# ユーザー一覧
def display_all():
    messages = Message.select()
    for m in messages:
        print(f"Name: {m.name} Age: {m.age}")


print("===== Welcome to CRM Application =====")
print("[S]how: Show all users info")
print("[A]dd: Add new user")
print("[Q]uit: Quit The Application")
print("======================================")
print("")


while True:

    user_com = input("Your command >")

    if user_com == "S":
        display_all()
        print("")

    elif user_com == "A":
        name_new = input("New user name >")
        age_new = input("New user age >")
        add_user(name_new, age_new)
        print(f"Add new user: {name_new}")
        print("")

    elif user_com == "Q":
        print("Bye!")
        break

    else:
        print("command not found")
        print("")
