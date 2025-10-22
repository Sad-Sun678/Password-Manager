import functions as fn
import FreeSimpleGUI as sg


label1 = sg.Text("Type in a Website")
label2 = sg.Text("Enter desired Number of upper case characters")
label3 = sg.Text("Enter desired number of lower case characters")
label4 = sg.Text("Enter desired number of numerical characters")
label5 = sg.Text("Enter desired number of special characters")
website_box = sg.InputText(tooltip = "Enter Website", key = "website")
upper_case_box = sg.InputText(tooltip = "Enter Desired Number of upper case characters",
                              key = "upper_case")
lower_case_box = sg.InputText(tooltip= "Enter desired number of lower case characters",
                              key = "lower_case")
numbers_box = sg.InputText(tooltip= "Enter desired number of numerical characters",
                              key = "lower_case")
special_box = sg.InputText(tooltip= "Enter desired number of special characters",
                              key = "lower_case")


submit_button = sg.Button("Generate")

window = sg.Window('My Password Manager', layout=[[[label1],[website_box]],
                                                  [[label2],[upper_case_box]],
                                                  [[label3],[lower_case_box]],
                                                  [[label4],[numbers_box]],
                                                  [[label5],[special_box]],
                                                  [submit_button]],
                   font=('Times New Roman', 20))
while True:
    event, values = window.read()
    print(event)

    match event:
        case 'Generate':
            values = fn.convert_to_int(values)
            my_list = fn.convert_to_list(values)
            password_generated = fn.create_new_password(*my_list)
            password = fn.shuffle_str(password_generated)
            print(f"the final result is {"".join(password)}")






window.close()
