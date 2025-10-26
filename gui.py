import os

import functions as fn
import FreeSimpleGUI as sg
import time
from functions import write_to_file

# Define needed elements
sg.theme("Black")
clock = sg.Text('', key='clock')
label1 = sg.Text("Type in a Website")
label2 = sg.Text("Enter desired number of upper case characters")
label3 = sg.Text("Enter desired number of lower case characters")
label4 = sg.Text("Enter desired number of numerical characters")
label5 = sg.Text("Enter desired number of special characters")
website_edit_desc_label = sg.Text("Enter new name of the website")

row1 = [sg.Text("Type in a Website", size=(35,1), justification='left'),
        sg.Input(key="website", expand_x=True)]

row2 = [sg.Text("Enter desired number of upper case characters", size=(35,1),
                justification='left'),
        sg.Input(key="upper_case", size=(2,1))]

row3 = [sg.Text("Enter desired number of lower case characters", size=(35,1),
                justification='left'),
        sg.Input(key="lower_case", size=(2,1))]

row4 = [sg.Text("Enter desired number of numerical characters", size=(35,1),
                justification='left'),
        sg.Input(key="number_case", size=(2,1))]

row5 = [sg.Text("Enter desired number of special characters", size=(35,1),
                justification='left'),
        sg.Input(key="special_case", size=(2,1))]


submit_button = sg.Button("Generate")
display_button = sg.Button("Display")

window = sg.Window(
    'My Password Manager',
    layout=[
        [clock],
        [row1],
        [row2],
        [row3],
        [row4],
        [row5],
        [submit_button, display_button],
    ],
    font=('Times New Roman', 15), element_padding=(10,5))





window2 = None
window2_open = False
while True:
    if os.path.exists("passwords.txt"):
        pass
    else:
        open("passwords.txt",'w')

    # polls window to receive updates
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:

        case 'Generate':
            try:
                website = values['website']

                values = fn.convert_to_int(values)
                my_list = fn.convert_to_list(values)
                password_generated = fn.create_new_password(*my_list)
                password = fn.shuffle_str(password_generated)
                password = "".join(password)
                fn.write_to_file(website, password)
                if window2_open and not window2.was_closed():
                    new_content = fn.view_file()
                    window2['passwords'].update(new_content)

                generate_popup = sg.popup("Password Generated",
                                          custom_text="Okay")
            except ValueError:
                sg.popup("Please type the desired number of characters into the relevant boxes",
                         custom_text = "Okay" )

        case 'Display':
            passwords_file = fn.view_file()
            formatted_passwords_file = fn.format_password_list(passwords_file)

            secrets_revealed = sg.Listbox(values=fn.view_file(), key='passwords',
                                          enable_events=True,
                                          size=[45, 10])
            edit_button = sg.Button("Regenerate")
            delete_button = sg.Button("Delete")

            window2 = sg.Window('Passwords Master List', layout=[[secrets_revealed],
                                                                 [[edit_button,delete_button]]],
                                font=('Times New Roman', 15))
            window2_open = True
            event, value = window2.read(timeout=0)

            match event:
                case sg.WIN_CLOSED:
                    break
    if window2 and not window2.was_closed():
        event2, values2 = window2.read(timeout=0)
        if event2 == sg.WIN_CLOSED:
            window2.close()
            window2 = None
            window2_open = False
        elif event2 == "Regenerate":
            try:
                password_to_edit = values2['passwords'][0]
                print(password_to_edit)
                pop_value = sg.popup_yes_no(f"Would you like to regenerate the password below?\n"
                                            f"{password_to_edit}")
                match pop_value:
                    case "Yes":
                        user_response = list(
                            sg.popup_get_text(f"Please enter the characters you would like in the new password"
                                              f" in the following format\n"
                                              f"upper,lower,numbers,special"))
                        regen_arguments = user_response
                        formatted_args = []
                        for i in regen_arguments:
                            if i == ',':
                                pass
                            else:
                                formatted_args.append(int(i))
                        regenerated_password = fn.create_new_password(*formatted_args)
                        regenerated_password = fn.shuffle_str(regenerated_password)
                        splits = password_to_edit.split(":")
                        website = splits[0]
                        formatted_password = fn.format_to_string(regenerated_password)
                        fn.write_to_file(website, formatted_password)
                        fn.delete_saved_password(password_to_edit)
                        new_content = fn.view_file()
                        window2['passwords'].update(new_content)
            except IndexError:
                sg.popup("Cannot regenerate. Nothing is selected",
                         custom_text="Okay")

        elif event2 == "Delete":
            try:
                password_to_delete = values2['passwords'][0]
                print(password_to_delete)
                pop_value2 = sg.popup_yes_no(f"Would you like to delete the password below?\n"
                                            f"{password_to_delete}")
                match pop_value2:
                    case "Yes":
                        fn.delete_saved_password(password_to_delete)
                        new_content = fn.view_file()
                        window2['passwords'].update(new_content)
            except IndexError:
                sg.popup("Cannot delete. Nothing is selected",
                         custom_text= "Okay")




window.close()



