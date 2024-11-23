import sys
from pathlib import Path
from colorama import Fore, Style

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        #current_dir = Path(__file__).parent
        #display_directory_structure(current_dir)
        print(Fore.RED + "Треба використовувати насутпний код: python Exercise3.py <шлях_до_директорії>")
    else:
        path = sys.argv[1]
        display_directory_structure(path)
