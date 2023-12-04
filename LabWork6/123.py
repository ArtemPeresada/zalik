import os
from pathlib import Path

def main():
    print("Ласкаво просимо до програми!")

    desktop_path = get_desktop_path()

    while True:
        print("\nОберіть опцію:")
        print("1. Введення даних")
        print("2. Виведення результатів")
        print("3. Видалення даних")
        print("4. Завершити роботу")

        choice = input("Ваш вибір: ")

        if choice == '1':
            input_data(desktop_path)
        elif choice == '2':
            output_results(desktop_path)
        elif choice == '3':
            delete_data(desktop_path)
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

def input_data(desktop_path):
    try:
        user_input = input("Введіть дані: ")
        
    except Exception as e:
        print(f"Помилка: {e}")
        return

    file_path = desktop_path / 'LW6.txt'

    try:
        with open(file_path, 'r') as file:
            previous_data = file.read()
    except FileNotFoundError:
        previous_data = ""

    with open(file_path, 'w') as file:
        file.write(previous_data + user_input + '\n')
    print("Дані успішно додано.")

def output_results(desktop_path):
    file_path = desktop_path / 'LW6.txt'

    try:
        with open(file_path, 'r') as file:
            data = file.read()
        print("Всі введені дані:", data)
    except FileNotFoundError:
        print("Файл з даними не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

def delete_data(desktop_path):
    file_path = desktop_path / 'LW6.txt'

    try:
        with open(file_path, 'w') as file:
            file.write("")
        print("Дані успішно видалено.")
    except Exception as e:
        print(f"Помилка під час видалення даних: {e}")

def get_desktop_path():
    desktop_path = Path.home() / "Desktop"
    return desktop_path

if __name__ == "__main__":
    main()
