def find_values_above_threshold(file_path, threshold):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                time, value_str = line.strip().split()

                if not value_str.isdigit():
                    print(f"Некоректне значення у рядку: {line}")
                    continue

                value = int(value_str)

                if value > threshold:
                    print(f"Час: {time}, Значення: {value}")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

threshold_value = int(input("Введіть значення AAA: "))

file_path = "workpy"  

find_values_above_threshold(file_path, threshold_value)
