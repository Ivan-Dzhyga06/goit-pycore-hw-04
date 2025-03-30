with open('text.txt', 'w') as information:
    information.write('''Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000''')  

def total_salary(path):
    with open(path, "r") as information:
        content = information.read()
    numbers = [int(part) for item in content.split("\n") for part in item.split(",") if part.strip().isdigit()]
    total = sum(numbers)
    average = int(total/3)
    return total, average


total, average = total_salary("text.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
