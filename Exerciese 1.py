def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                _, salary = line.strip().split(',')
                total += int(salary)
                count += 1

            average = total / count if count > 0 else 0
            return total, average

    except FileNotFoundError:
        print("Файлу немає")
    except ValueError:
        print("Хибний формат данних")
    except Exception as e:
        print(f"Трапилася помилка: {e}")