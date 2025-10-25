# functions.py
import random, string
from pathlib import Path

def shuffle_str(elements):
    working_list = elements
    random.shuffle(working_list)
    return working_list



def create_new_password(upper_case, lower_case, numbers,special_char):
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
        file.write(f"{website}: {password}\n")
def delete_saved_password(line_in_file):
    content = view_file()
    out_path = Path(__file__).parent / "passwords.txt"
    if line_in_file in content:
        content.remove(line_in_file)
        with open ("passwords.txt",'w') as file:
            file.writelines(content)

def write_lines(line):
    with open("passwords.txt",'w') as file:
        file.writelines(line)

def view_file(filename = "passwords.txt"):
    header = 'website, password\n'
    with open(filename, 'r') as file:
        content = file.readlines()
        if header in content:
            content.remove(header)
        return content


def convert_to_int(dictionary):
    for key, value in dictionary.items():
        if key == "website":
            pass
        else:
            converted_value = int(value)
            dictionary[key] = converted_value
    return dictionary

def convert_to_list(dictionary):
    list = []
    for k, v in dictionary.items():
        if k == 'website':
            pass
        else:
            list.append(dictionary[k])
    return list

def format_password_list(lines):
    formatted = ""
    for line in lines:
        stripped = line.strip()
        if stripped:
            formatted += stripped + "\n"
    return formatted
def format_to_string(lines):
    formatted = ''.join(lines)
    return formatted
def format_password_list_regen_mode(lines):
    formatted = ""
    for line in lines:
        stripped = line.strip()
        if stripped:
            formatted += stripped
    return formatted

