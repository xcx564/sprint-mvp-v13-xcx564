# ===== T-1. Главное меню (общая задача) =====
TITLE = "Коммунальные платежи"  # впишите название своего продукта
MENU = []  # пункты меню: (название, функция)


def ask_int(text):
    # спрашивает целое число, пока его не введут правильно
    while True:
        value = input(text).strip()
        if value.lstrip("-").isdigit():
            return int(value)
        print("Ошибка: введите целое число")


def ask_float(text):
    # спрашивает число (можно дробное), пока его не введут правильно
    while True:
        value = input(text).strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Ошибка: введите число")


def start():
    while True:
        print()
        print("=====", TITLE, "=====")
        for number, item in enumerate(MENU, start=1):
            print(number, "-", item[0])
        print("0 - Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(MENU):
            MENU[int(choice) - 1][1]()
        else:
            print("Нет такого пункта меню")


# ===== US-2. Ввод показаний воды =====
readings = {}  # показания счётчиков
bills = {}  # услуга -> сумма к оплате


def enter_water():
    readings["хол_было"] = ask_float("Холодная вода, прошлые показания: ")
    readings["хол_стало"] = ask_float("Холодная вода, текущие показания: ")
    readings["гор_было"] = ask_float("Горячая вода, прошлые показания: ")
    readings["гор_стало"] = ask_float("Горячая вода, текущие показания: ")
    print("Показания сохранены")


MENU.append(("Ввести показания воды", enter_water))


# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()
