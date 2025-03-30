import sys
import os
from colorama import Fore, init
from pathlib import Path

init(autoreset=True)

def print_directory_structure(directory: Path, indent: str = ""):
    try:
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for item in items:
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}")
                print_directory_structure(item, indent + " ┃ ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Доступ заборонено: {directory}")

if len(sys.argv) < 2:
    print(f"{Fore.RED}Необхідно вказати шлях до директорії!")
    sys.exit(1)

directory_path = Path(sys.argv[1])


if not directory_path.exists() or not directory_path.is_dir():
    print(f"{Fore.RED}Вказаний шлях не є директорією або не існує!")
    sys.exit(1)

print(f"{Fore.YELLOW}📦 {directory_path.resolve()}")
print_directory_structure(directory_path)