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


# ===== US-3. Стоимость воды =====
COLD_TARIFF = 58.0  # руб. за 1 куб. м (условный тариф)
HOT_TARIFF = 300.0  # руб. за 1 куб. м (условный тариф)


def water_cost():
    if "хол_было" not in readings:
        print("Сначала введите показания воды")
        return
    cold = readings["хол_стало"] - readings["хол_было"]
    hot = readings["гор_стало"] - readings["гор_было"]
    cold_cost = cold * COLD_TARIFF
    hot_cost = hot * HOT_TARIFF
    bills["Холодная вода"] = cold_cost
    bills["Горячая вода"] = hot_cost
    print(f"Холодная вода: {cold:.2f} куб. м — {cold_cost:.2f} руб.")
    print(f"Горячая вода: {hot:.2f} куб. м — {hot_cost:.2f} руб.")


MENU.append(("Рассчитать стоимость воды", water_cost))


# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()
