from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from File_manager import *
from validators import *
from datetime import datetime

person_list = read_from_file("persons.dat")


def load_data(person_list):
    person_list = read_from_file("persons.dat")
    for row in table.get_children():
        table.delete(row)

    if person_list:
        for person in person_list:
           table.insert("", END, values=person)


def reset_form():
    id.set(len(person_list) + 1)
    Esmdars.set("")
    Grade.set("")
    Teacher.set("")
    Startdate.set("")
    Duration.set(0)
    load_data(person_list)


def save_btn_click():
    person = (id.get(), Esmdars.get(), Grade.get(), Teacher.get(),Startdate.get(), Duration.get())
    errors = person_validator(person)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Person saved")
        person_list.append(person)
        write_to_file("persons.dat", person_list)
        reset_form()


def table_select(x):
    selected_person = table.item(table.focus())["values"]
    if selected_person:
        id.set(selected_person[0])
        Esmdars.set(selected_person[1])
        Grade.set(selected_person[2])
        Teacher.set(selected_person[3])
        Startdate.set(selected_person[4])
        Duration.set(selected_person[5])


def edit_btn_click():
    pass


def remove_btn_click():
    pass


window = Tk()
window.title("Person Info")
window.geometry("800x330")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

#Esmdars
Label(window, text="esmdars").place(x=20, y=60)
Esmdars = StringVar()
Entry(window, textvariable=Esmdars).place(x=80, y=60)

# Grade
Label(window, text="grade").place(x=20, y=100)
Grade = IntVar()
Entry(window, textvariable=Grade).place(x=80, y=100)

# Teacher
Label(window, text="teacher").place(x=20, y=140)
Teacher = StringVar()
Entry(window, textvariable=Teacher).place(x=80, y=140)

#Startdate
Label(window, text="startdate").place(x=20, y=180)
Startdate = StringVar(value="2024-01-01")
Entry(window, textvariable=Startdate).place(x=80, y=180)

#Duration
Label(window, text="duration").place(x=20, y=220)
Duration = IntVar()
Entry(window, textvariable=Duration).place(x=80, y=220)

table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5 , 6 ], show="headings")
table.heading(1, text="Id")
table.heading(2, text="esmdars")
table.heading(3, text="grade")
table.heading(4, text="teacher")
table.heading(5, text="startdate")
table.heading(6, text="Duration")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)

table.bind("<<TreeviewSelect>>", table_select)

table.place(x=230, y=20, width=550, height=285)

Button(window, text="Save", width=6, command=save_btn_click).place(x=20, y=280)
Button(window, text="Edit", width=6, command=edit_btn_click).place(x=90, y=280)
Button(window, text="Remove", width=6, command=remove_btn_click).place(x=160, y=280)
Button(window, text="Clear", width=6, command=reset_form).place(x=20, y=250, width=190)

reset_form()

window.mainloop()
