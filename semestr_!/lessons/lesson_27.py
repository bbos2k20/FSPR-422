USERS = [
    {
        "name": "mirabbos",
        "email": "mirabbos@gmail.com",
        "password": "qwerty",
        "card": {"code": "0987098778907890", "balance": 5000},
    }
]


class Store:
    purches = []

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.email = email
        self.password = password
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        for user in USERS:
            if user["email"] == email or user["password"] == password:
                return "Wrong email or password."
            else:
                break

        if not (name and email and password and card_code and card_balance):
            return "Empty vaules were given."

        if (
            name.isalpha()
            and "@" in email
            and len(password) >= 6
            and len(card_code) == 16
        ):
            USERS.append(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                    "card": {"code": card_code, "balance": card_balance},
                }
            )
            return cls(name, email, password, card_code, card_balance)
        else:
            return "Wrong credentials"

    @classmethod
    def login(cls, email, password):
        if (email and password) in USERS:
            print("Добро пожаловать!")
        else:
            return "Пройдите рег"


enter_method = input("Choose method: register or login: ")
if enter_method == "register":
    user_1 = Store.register(
        "Abbos", "mirabbos223@gmail.com", "123asda", "1234123443214321", 5000
    )
if enter_method == "login":
    user_1 = Store.login("mirabbos223@gmail.com", "123asda")

print(user_1)
print(user_1.name, user_1.email, user_1.password)
for user in USERS:
    print(user)
