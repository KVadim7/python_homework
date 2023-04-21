import json

PHONEBOOK_FILE = "phonebook.json"

def load_phonebook():
    try:
        with open(PHONEBOOK_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, "w") as f:
        json.dump(phonebook, f, indent=4)


def add_entry(phonebook):
    print("Add new entry")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    telephone_number = input("Telephone number: ")
    city = input("City: ")
    state = input("State: ")
    entry = {
        "first_name": first_name,
        "last_name": last_name,
        "telephone_number": telephone_number,
        "city": city,
        "state": state,
    }
    phonebook[telephone_number] = entry
    print("Entry added")


def search_by_first_name(phonebook):
    print("Search by first name")
    first_name = input("First name: ")
    results = [entry for entry in phonebook.values() if entry["first_name"].lower() == first_name.lower()]
    print_results(results)


def search_by_last_name(phonebook):
    print("Search by last name")
    last_name = input("Last name: ")
    results = [entry for entry in phonebook.values() if entry["last_name"].lower() == last_name.lower()]
    print_results(results)


def search_by_full_name(phonebook):
    print("Search by full name")
    full_name = input("Full name: ")
    results = [entry for entry in phonebook.values() if f"{entry['first_name']} {entry['last_name']}".lower() == full_name.lower()]
    print_results(results)


def search_by_telephone_number(phonebook):
    print("Search by telephone number")
    telephone_number = input("Telephone number: ")
    entry = phonebook.get(telephone_number)
    if entry:
        print_entry(entry)
    else:
        print("No entry found")


def search_by_city_or_state(phonebook):
    print("Search by city or state")
    query = input("City or state: ")
    results = [entry for entry in phonebook.values() if entry["city"].lower() == query.lower() or entry["state"].lower() == query.lower()]
    print_results(results)


def delete_entry(phonebook):
    print("Delete entry")
    telephone_number = input("Telephone number: ")
    entry = phonebook.pop(telephone_number, None)
    if entry:
        print("Entry deleted")
    else:
        print("No entry found")


def update_entry(phonebook):
    print("Update entry")
    telephone_number = input("Telephone number: ")
    entry = phonebook.get(telephone_number)
    if entry:
        print("Current entry:")
        print_entry(entry)
        first_name = input("First name [leave empty to keep current value]: ")
        last_name = input("Last name [leave empty to keep current value]: ")
        telephone_number = input("Telephone number [leave empty to keep current value]: ")
        city = input("City [leave empty to keep current value]: ")
        state = input("State [leave empty to keep current value]: ")
        if first_name:
            entry["first_name"] = first_name
        if last_name:
            entry["last_name"] = last_name
        if telephone_number:
            entry["telephone_number"] = telephone_number
        if city:
            entry["city"] = city
        if state:
            entry["state"] = state
        print("Entry updated")


def print_entry(entry):
    print(f"First name: {entry['first_name']}")
    print(f"Last name: {entry['last_name']}")
    print(f"Telephone number: {entry['telephone_number']}")
    print(f"City: {entry['city']}")
    print(f"State: {entry['state']}")


def print_results(results):
    if results:
        for i, entry in enumerate(results):
            print(f"Result {i + 1}")
            print_entry(entry)
    else:
        print("No results found")


def main():
    phonebook = load_phonebook()
    while True:
        print("\nPhonebook")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete an entry")
        print("8. Update an entry")
        print("9. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_entry(phonebook)
        elif choice == "2":
            search_by_first_name(phonebook)
        elif choice == "3":
            search_by_last_name(phonebook)
        elif choice == "4":
            search_by_full_name(phonebook)
        elif choice == "5":
            search_by_telephone_number(phonebook)
        elif choice == "6":
            search_by_city_or_state(phonebook)
        elif choice == "7":
            delete_entry(phonebook)
        elif choice == "8":
            update_entry(phonebook)
        elif choice == "9":
            save_phonebook(phonebook)
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
