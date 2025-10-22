# main.py
import functions as fn
import time
from functions import write_to_file

while True:
    border = "=" * 27
    user_selection = input(
        "Welcome to PyPass password manager. What would you like to do?\n"
        "1. Create New Password\n"
        "2. View Saved Passwords\n"
        "> "
    ).strip().lower()

    if user_selection in ("1", "create"):
        website = input("What website is this for? ").strip()
        upper_case = int(input("Enter how many will be upper case: ").strip())
        lower_case = int(input("Enter how many will be lower case: ").strip())
        special_char = int(input("Enter the number of special characters: ").strip())
        numbers = int(input("Enter the number of digits: ").strip())


        unshuffled_password = fn.create_new_password(upper_case, lower_case, special_char,numbers)
        password_as_list = fn.shuffle_str(unshuffled_password)
        password = "".join(password_as_list)
        write_to_file(website, password)

        print(f"Your new password for {website} is: {password}")

    elif user_selection in ("2", "view"):
        fn.print_box_from_file('passwords.txt', "Saved Passwords")
    else:
        print("Invalid choice.\n")
