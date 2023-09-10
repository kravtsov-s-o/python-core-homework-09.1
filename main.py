contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
        except Exception as e:
            return f"Error: {str(e)}"

    return wrapper

@input_error
def add_contact(command):
    parts = command.split(" ")
    if len(parts) == 3:
        name, phone = parts[1], parts[2]
        if name not in contacts:
            contacts[name] = phone
            return f"Contact {name} with number {phone} saved."
        else:
            return "Contact with the same name already exists"
    else:
        raise ValueError


@input_error
def change_contact(command):
    parts = command.split(" ")
    if len(parts) == 3:
        name, phone = parts[1], parts[2]
        if name in contacts:
            contacts[name] = phone
            return f"Phone number for {name} changed to {phone}."
        else:
            raise KeyError
    else:
        raise ValueError


@input_error
def get_phone(command):
    parts = command.split(" ")
    if len(parts) == 2:
        name = parts[1]
        if name in contacts:
            return f"Phone number for {name}: {contacts[name]}"
        else:
            raise KeyError
    else:
        raise ValueError


@input_error
def show_all_contacts():
    result = "Contacts list:\n"
    contact_strings = [f"{name}: {phone}" for name, phone in contacts.items()]
    result += "\n".join(contact_strings)
    return result

def main():
    while True:
        command = input("Write command: ").strip()

        if command.lower() == "hello":
            print("How can I help you?")
        elif command.lower().startswith("add "):
            print(add_contact(command))
        elif command.lower().startswith("change "):
            print(change_contact(command))
        elif command.lower().startswith("phone "):
            print(get_phone(command))
        elif command.lower() == "show all":
            print(show_all_contacts())
        elif command.lower() in [".", "good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Write 'hello', 'add', 'change', 'phone', 'show all' or 'exit'.")


if __name__ == '__main__':
    main()
