from datetime import date
from tkinter import *
from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from controller.patient_controller import *
import tkinter.messagebox as msg


class PatientView:

    def destroy_window(self):
        self.win.destroy()

    def save_click(self):
        data = save_patient(self.name.variable.get(), self.family.variable.get(), self.age.variable.get(),
                            self.gender.variable.get(), self.contact_info.variable.get(),
                            self.date_of_registration.variable.get())
        if data[0] == True:
            msg.showinfo("Save", f"Patient Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data[1]}")

    def edit_click(self):
        data = edit_patient(self.id.variable.get(), self.name.variable.get(), self.family.variable.get(),
                            self.age.variable.get(), self.gender.variable.get(), self.contact_info.variable.get(),
                            self.date_of_registration.variable.get())
        if data[0] == True:
            msg.showinfo("Edit", f"Patient Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data[1]}")

    def remove_click(self):
        data = remove_patient_by_id(self.id.variable.get(), self.name.variable.get(), self.family.variable.get(),
                                    self.age.variable.get(), self.gender.variable.get(),
                                    self.contact_info.variable.get(),
                                    self.date_of_registration.variable.get())
        if data[0] == True:
            msg.showinfo("Remove", f"Patient Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data[1]}")

    def select_table(self, selected_patient):
        self.id.variable.set(selected_patient[0])
        self.name.variable.set(selected_patient[1])
        self.family.variable.set(selected_patient[2])
        self.age.variable.set(selected_patient[3])
        self.gender.variable.set(selected_patient[4])
        self.contact_info.variable.set(selected_patient[5])
        self.date_of_registration.variable.set(selected_patient[6])

    def reset_form(self):
        self.id.variable.set(0)
        self.name.variable.set("")
        self.family.variable.set("")
        self.age.variable.set("")
        self.gender.variable.set("")
        self.contact_info.variable.set("")
        self.date_of_registration.variable.set("")
        patient_list = find_all_patients()
        self.table.refresh_table(patient_list)

    def set_today(self):
        self.date_of_registration.variable.set(date.today().strftime("%Y-%m-%d"))

    def show_patients(self):
        patient_list = find_all_patients()
        self.table.refresh_table(patient_list)

    def __init__(self, title, geometry, open_doctors_command=None, open_records_command=None,
                 open_appointments_command=None):
        self.win = Tk()
        self.win.geometry(geometry)
        self.win.title(title)
        Label(self.win, text="Patients", font=("Arial", 20)).place(x=20, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 80, data_type="int")
        self.name = LabelAndEntry(self.win, "Name", 20, 110, data_type="str")
        self.family = LabelAndEntry(self.win, "Family", 20, 140, data_type="str")
        self.age = LabelAndEntry(self.win, "Age", 20, 170, data_type="str")
        self.gender = LabelAndEntry(self.win, "Gender", 20, 200, data_type="str")
        self.contact_info = LabelAndEntry(self.win, "Contact Info            09", 20, 230, data_type="int")
        self.date_of_registration = LabelAndEntry(self.win, "Date of Registration", 20, 260, data_type="str")
        self.table = Table(self.win, ["ID", "Name", "Family", "Age", "Gender", "Contact Info", "Date of Registration"],
                           [10, 50, 50, 40, 50, 90, 140], 300, 50, self.select_table)

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=340)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=310)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=310)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=310)
        Button(self.win, text="Show Patients", width=12, command=self.show_patients).place(x=90, y=340)
        Button(self.win, text="Set today", width=7, command=self.set_today, font=("Arial", 8)).place(x=150, y=280)
        self.open_doctors = Button(self.win, text="Open Doctors", width=10, command=lambda: open_doctors_command(self))
        self.open_doctors.place(x=300, y=340)
        self.open_records = Button(self.win, text="Open Medical Records", width=18,
                                   command=lambda: open_records_command(self))
        self.open_records.place(x=390, y=340)
        self.open_appointment = Button(self.win, text="Open Appointments", width=18,
                                       command=lambda: open_appointments_command(self))
        self.open_appointment.place(x=535, y=340)

        self.win.mainloop()
