available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive",
}

current_choice = None
computer_parts = {} # Create an empty dictionary

while current_choice != "0":

    # "in" checks for keys in a dictionary
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # It's already in it, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            # using f string instead of .format
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
    else:
        print("Please choose from the below list!")
        for key, part in available_parts.items():
            print(key, part, sep=": ")
        print("0: to finish")

    current_choice = input(">")


    
