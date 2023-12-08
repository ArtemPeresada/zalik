def find_values_above_threshold(file_path, threshold):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Розділити рядок на час і значення
                time, value_str = line.strip().split()

                # Перевірити, чи введене значення є числом
                if not value_str.isdigit():
                    print(f"Некоректне значення у рядку: {line}")
                    continue

                value = int(value_str)

                # Порівняти значення з пороговим значенням AAA
                if value > threshold:
                    print(f"Час: {time}, Значення: {value}")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

# Отримати введення від користувача
threshold_value = int(input("Введіть значення AAA: "))

# Задати шлях до текстового файлу
file_path = "workpy"  # Замініть на реальний шлях до вашого файлу

# Викликати функцію для знаходження і виведення значень, які перевищують порогове значення
find_values_above_threshold(file_path, threshold_value)
