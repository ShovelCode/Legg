# Simple Text Adventure (vanilla Python 3)

# --- World Definition ---

rooms = {
    "start": {
        "description": "You are in a dimly lit room. There is a door to the north.",
        "exits": {"north": "hall"},
    },
    "hall": {
        "description": "You are in a long hallway. Doors lead south and east.",
        "exits": {"south": "start", "east": "treasure"},
    },
    "treasure": {
        "description": "You found the treasure room! A chest sits in the center.",
        "exits": {"west": "hall"},
        "item": "treasure"
    }
}

player = {
    "location": "start",
    "inventory": []
}

# --- Game Logic ---

def describe_location():
    room = rooms[player["location"]]
    print("\n" + room["description"])

    if "item" in room:
        print(f"You see a {room['item']} here.")

    print("Exits:", ", ".join(room["exits"].keys()))


def move(direction):
    room = rooms[player["location"]]
    if direction in room["exits"]:
        player["location"] = room["exits"][direction]
        print(f"You go {direction}.")
    else:
        print("You can't go that way.")


def take(item):
    room = rooms[player["location"]]
    if room.get("item") == item:
        player["inventory"].append(item)
        del room["item"]
        print(f"You take the {item}.")
    else:
        print("There is no such item here.")


def show_inventory():
    if player["inventory"]:
        print("You have:", ", ".join(player["inventory"]))
    else:
        print("You are carrying nothing.")


def help_menu():
    print("""
Commands:
  go [direction]
  take [item]
  inventory
  help
  quit
""")


# --- Game Loop ---

def main():
    print("Welcome to the Text Adventure.")
    print("Type 'help' for commands.")

    while True:
        describe_location()
        command = input("\n> ").strip().lower().split()

        if not command:
            continue

        if command[0] == "go" and len(command) > 1:
            move(command[1])
        elif command[0] == "take" and len(command) > 1:
            take(command[1])
        elif command[0] == "inventory":
            show_inventory()
        elif command[0] == "help":
            help_menu()
        elif command[0] == "quit":
            print("Goodbye.")
            break
        else:
            print("I don't understand that command.")


if __name__ == "__main__":
    main()
