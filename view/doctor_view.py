from tkinter import *
from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from controller.doctor_controller import *
import tkinter.messagebox as msg


class DoctorView:

    def save_click(self):
        data = save_doctor(self.name.variable.get(), self.family.variable.get(), self.specialization.variable.get(),
                           self.contact_info.variable.get())
        if data[0] == True:
            msg.showinfo("Save", f"Doctor Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data[1]}")

    def edit_click(self):
        data = edit_doctor(self.id.variable.get(), self.name.variable.get(), self.family.variable.get(), self.specialization.variable.get(),
                           self.contact_info.variable.get())
        if data[0] == True:
            msg.showinfo("Edit", f"Doctor Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data[1]}")

    def remove_click(self):
        data = remove_doctor_by_id(self.id.variable.get() ,self.name.variable.get(), self.family.variable.get(), self.specialization.variable.get(),
                                   self.contact_info.variable.get())
        if data[0] == True:
            msg.showinfo("Remove", f"Doctor Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data[1]}")

    def select_table(self, selected_doctor):
        self.id.variable.set(selected_doctor[0])
        self.name.variable.set(selected_doctor[1])
        self.family.variable.set(selected_doctor[2])
        self.specialization.variable.set(selected_doctor[3])
        self.contact_info.variable.set(selected_doctor[4])

    def reset_form(self):
        self.id.variable.set(0)
        self.name.variable.set("")
        self.family.variable.set("")
        self.specialization.variable.set("")
        self.contact_info.variable.set("")
        doctor_list = find_all_doctors()
        self.table.refresh_table(doctor_list)

    def show_doctors(self):
        doctor_list = find_all_doctors()
        self.table.refresh_table(doctor_list)


    def __init__(self, title, geometry):
        self.win = Tk()
        self.win.geometry(geometry)
        self.win.title(title)
        Label(self.win, text="Doctors", font=("Arial", 20)).place(x=20, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 80, data_type="int")
        self.name = LabelAndEntry(self.win, "Name", 20, 110, data_type="str")
        self.family = LabelAndEntry(self.win, "Family", 20, 140, data_type="str")
        self.specialization = LabelAndEntry(self.win, "Specialization", 20, 170, data_type="str")
        self.contact_info = LabelAndEntry(self.win, "Contact Info            09", 20, 200, data_type="int")

        self.table = Table(self.win, ["ID", "Name", "Family", "Specialization", "Contact Info"],
                           [10, 60, 60, 80, 90], 300, 50, self.select_table)

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=310)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=280)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=280)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=280)
        Button(self.win, text="Show Doctors", width=12, command=self.show_doctors).place(x=90, y=310)


        self.win.mainloop()


#ui = DoctorView("Doctor View", "620x370")
