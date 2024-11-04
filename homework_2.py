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



def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_info)

    except FileNotFoundError:
        print("Файлу немає")
    except ValueError:
        print("Хибний формат данних")
    except Exception as e:
        print(f"Трапилася помилка: {e}")

    return cats_info


from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def display_directory_structure(path, level=0):
    try:
        directory = Path(path)

        if not directory.exists() or not directory.is_dir():
            print(Fore.RED + "Помилка: Вказаний шлях не існує або не є директорією.")
            return

        for item in directory.iterdir():
            indent = '    ' * level  
            if item.is_dir():
                print(f"{indent}{Fore.GREEN}{item.name}/")
                display_directory_structure(item, level + 1)
            else:
                print(f"{indent}{Fore.BLUE}{item.name}")
    except Exception as e:
        print(Fore.RED + f"Виникла помилка: {e}")
        





def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid command format. Use: add [name] [phone]"

def change_contact(args, contacts):
    try:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid command format. Use: change [name] [new_phone]"

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    except IndexError:
        return "Invalid command format. Use: phone [name]"

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()