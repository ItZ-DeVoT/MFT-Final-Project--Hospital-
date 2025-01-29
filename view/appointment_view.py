from datetime import date
from tkinter import *

from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from controller.appointment_controller import *
import tkinter.messagebox as msg


class AppointmentView:

    def save_click(self):
        data = save_appointment(self.patient.variable.get(), self.doctor.variable.get(),
                                self.appointment_date.variable.get(), self.status_var.get())
        if data[0] == True:
            msg.showinfo("Save", f"Appointment Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data[1]}")

    def edit_click(self):
        data = edit_appointment(self.id.variable.get(), self.patient.variable.get(), self.doctor.variable.get(),
                                self.appointment_date.variable.get(), self.status_var.get())
        if data[0] == True:
            msg.showinfo("Edit", f"Appointment Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data[1]}")

    def remove_click(self):
        data = remove_appointment_by_id(self.id.variable.get(), self.patient.variable.get(), self.doctor.variable.get(),
                                        self.appointment_date.variable.get(), self.status_var.get())
        if data == True:
            msg.showinfo("Remove", f"Appointment Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data[1]}")

    def select_table(self, selected_appointment):
        self.id.variable.set(selected_appointment[0])
        self.patient.variable.set(selected_appointment[1])
        self.doctor.variable.set(selected_appointment[2])
        self.appointment_date.variable.set(selected_appointment[3])

    def reset_form(self):
        self.id.variable.set(0)
        self.patient.variable.set("")
        self.doctor.variable.set("")
        self.appointment_date.variable.set("")
        appointment_list = find_all_appointments()
        self.table.refresh_table(appointment_list)

    def show_appointments(self):
        record_list = find_all_appointments()
        if record_list == []:
            msg.showerror("Appointments", "No Appointment Found")
        else:
            self.table.refresh_table(record_list)

    def set_today(self):
        self.appointment_date.variable.set(date.today().strftime("%Y-%m-%d"))

    def __init__(self, title, geometry):
        self.win = Tk()
        self.win.geometry(geometry)
        self.win.title(title)
        Label(self.win, text="Medical Appointments", font=("Arial", 20)).place(x=20, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 80, data_type="int")
        self.patient = LabelAndEntry(self.win, "Patient ID", 20, 110, data_type="int")
        self.doctor = LabelAndEntry(self.win, "Doctor ID", 20, 140, data_type="int")
        self.appointment_date = LabelAndEntry(self.win, "Appointment date", 20, 170, data_type="str")
        self.status_var = StringVar(value="Undone")
        self.status = Label(self.win, text="Status :")
        self.status.place(x=20, y=200)
        Radiobutton(self.win, text="Done", variable=self.status_var, value="done").place(x=20, y=220)
        Radiobutton(self.win, text="Undone", variable=self.status_var, value="undone").place(x=20, y=240)
        Radiobutton(self.win, text="In progress", variable=self.status_var, value="in progress").place(x=20, y=260)

        self.table = Table(self.win, ["ID", "Patient ID", "Doctor ID", "Appointment date", "Status"],
                           [20, 80, 80, 120, 90], 300, 50, self.select_table)

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=330)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=300)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=300)
        Button(self.win, text="Show Appointments", width=18, command=self.show_appointments).place(x=90, y=330)
        Button(self.win, text="Set today", width=7, command=self.set_today, font=("Arial", 8)).place(x=150, y=200)

        self.win.mainloop()

# ui = AppointmentView("Medical Appointment View", "680x370")
