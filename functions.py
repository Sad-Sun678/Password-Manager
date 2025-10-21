# functions.py
import random, string
from pathlib import Path
def shuffle_str(list):
    shuffled_password = []
    for i in list:
        shuffled_password.append(random.choice(list))
    return shuffled_password



def create_new_password(upper_case, lower_case, special_char,numbers):
    password = []
    for _ in range(upper_case):
        password.append(random.choice(string.ascii_uppercase))
    for _ in range(lower_case):
        password.append(random.choice(string.ascii_lowercase))
    for _ in range(special_char):
        password.append(random.choice(string.punctuation))
    for _ in range(numbers):
        number = str(random.randint(1,9))
        password.append(number)
    return password

def write_to_file(website, password):
    out_path = Path(__file__).parent / "passwords.txt"
    with open(out_path, "a", encoding="utf-8") as file:
        file.write(f"{website}:{password}\n")

def view_file(filename = "passwords.txt"):
    with open(filename, 'r') as file:
        content = file.readlines()
    return content

def print_box_from_file(file_path, title=None):
    # Read all non-empty lines and strip whitespace
    with open(file_path, 'r') as file:
        items = [line.strip() for line in file if line.strip()]

    if not items:
        print("No items found in file.")
        return

    # Find the longest line
    max_len = max(len(line) for line in items)

    # Add some horizontal padding inside the box
    padding = 4
    box_width = max_len + padding

    # Build the title line if provided
    if title:
        title_line = f" {title} "
        title_padding = (box_width - len(title_line)) // 2
        print(" " * title_padding + title_line)

    # Top border
    print("+" + "-" * box_width + "+")

    # Center each line
    for line in items:
        line_padding = (box_width - len(line)) // 2
        print("|" + " " * line_padding + line + " " * (box_width - len(line) - line_padding) + "|")

    # Bottom border
    print("+" + "-" * box_width + "+")