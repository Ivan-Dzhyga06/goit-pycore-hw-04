def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    with open("contact_info.txt", "a") as contact_info:
        contact_info.write(f"Name: {name} \nPhone number: {phone}\n\n")
    return "Contact added."

def change_contact(args, contacts):   
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            print(f"{name} find. Phone number: {contacts[name]}")
            user_input = input("Do u want change number phone? (yes/no): ").lower()
            if user_input == "yes":
                new_phone = input("Please write new number: ")
                contacts[name] = new_phone
                return "Phone number changed"
            else:
                return "Phone number was not changed"
        else:
            return "Sorry, we didnt find this name"
    else:
        return "Please enter correct name"
    
def database(contacts):
     with open("contact_info.txt", "r") as contact_info:
        lines = contact_info.readlines()
        name = None
        phone = None
        for line in lines:
            line = line.strip()
            if line.startswith("Name:"):
                name = line.split(":", 1)[1].strip()
            elif line.startswith("Phone number:"):
                phone = line.split(":", 1)[1].strip()
                if name:
                    contacts[name] = phone
                    name = None
                    phone = None

def all_contacts(contacts):
    for name, phone in contacts.items():
        print(f"Name: {name} Phone number: {phone}")

def user_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"{name} is in base. Phone number: {contacts[name]}"
        else:
            return f"Sorry, we didnt find {name}"


def main():
    contacts = {}
    database(contacts)
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            all_contacts(contacts)
        elif command == "phone":
            print(user_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
