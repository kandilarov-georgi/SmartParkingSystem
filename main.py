from pymongo import MongoClient
from datetime import datetime

# Свързване към MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['Smart_Parking_System']  # Уверете се, че името на базата данни съвпада

def show_menu():
    print("\n-- Smart Parking System --")
    print("1. Показване на всички транзакции")
    print("2. Добавяне на нова транзакция")
    print("3. Изход")

def list_transactions():
    transactions = db.transactions.find()
    if db.transactions.count_documents({}) == 0:  # Ако няма транзакции, покажи съобщение
        print("Няма налични транзакции.")
    else:
        for t in transactions:
            print(t)

def add_transaction():
    user_id = input("Въведи ID на потребителя: ")
    reservation_id = input("Въведи ID на резервацията: ")
    amount = float(input("Въведи сума: "))
    payment_method = input("Метод на плащане (card/cash): ")

    transaction = {
        "user_id": user_id,
        "reservation_id": reservation_id,
        "amount": amount,
        "currency": "BGN",
        "payment_method": payment_method,
        "timestamp": datetime.now()
    }
    try:
        db.transactions.insert_one(transaction)  # Вмъкване на транзакцията в базата данни
        print("Транзакцията е добавена успешно!")
    except Exception as e:
        print(f"Грешка при добавяне на транзакцията: {e}")

# Основна програма
while True:
    show_menu()
    choice = input("Избор: ")

    if choice == "1":
        list_transactions()
    elif choice == "2":
        add_transaction()
    elif choice == "3":
        print("Изход...")
        break
    else:
        print("Невалиден избор, опитай пак!")
