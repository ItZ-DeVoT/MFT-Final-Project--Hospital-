from datetime import date
from tkinter import *
from view.component.table import Table
from view.component.label_and_entry import LabelAndEntry
from controller.medical_record_controller import *
import tkinter.messagebox as msg


class MedicalRecordView:

    def save_click(self):
        data = save_record(self.patient.variable.get(), self.diagnosis.variable.get(),
                           self.treatment_plan.variable.get(), self.visit_date.variable.get())
        if data[0] == True:
            msg.showinfo("Save", f"Record Saved")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data[1]}")

    def edit_click(self):
        data = edit_record(self.id.variable.get(), self.patient.variable.get(), self.diagnosis.variable.get(),
                           self.treatment_plan.variable.get(), self.visit_date.variable.get())
        if data[0] == True:
            msg.showinfo("Edit", f"Record Edited")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data[1]}")

    def remove_click(self):
        data = remove_medical_record_by_id(self.id.variable.get(), self.patient.variable.get(),
                                           self.diagnosis.variable.get(),
                                           self.treatment_plan.variable.get(), self.visit_date.variable.get())
        if data == True:
            msg.showinfo("Remove", f"Record Removed")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data[1]}")

    def select_table(self, selected_record):
        self.id.variable.set(selected_record[0])
        self.patient.variable.set(selected_record[1])
        self.diagnosis.variable.set(selected_record[2])
        self.treatment_plan.variable.set(selected_record[3])
        self.visit_date.variable.set(selected_record[4])

    def reset_form(self):
        self.id.variable.set(0)
        self.patient.variable.set("")
        self.diagnosis.variable.set("")
        self.treatment_plan.variable.set("")
        self.visit_date.variable.set("")
        record_list = find_all_medical_records()
        self.table.refresh_table(record_list)


    def show_records(self):
        record_list = find_all_medical_records()
        if record_list == []:
            msg.showerror("Records", "No Records Found")
        else:
            self.table.refresh_table(record_list)

    def set_today(self):
        self.visit_date.variable.set(date.today().strftime("%Y-%m-%d"))


    def __init__(self, title, geometry):
        self.win = Tk()
        self.win.geometry(geometry)
        self.win.title(title)
        Label(self.win, text="Medical Records", font=("Arial", 20)).place(x=20, y=10)
        self.id = LabelAndEntry(self.win, "ID", 20, 80, data_type="int")
        self.patient = LabelAndEntry(self.win, "Patient ID", 20, 110, data_type="int")
        self.diagnosis = LabelAndEntry(self.win, "Diagnosis", 20, 140, data_type="str")
        self.treatment_plan = LabelAndEntry(self.win, "Treatment plan", 20, 170, data_type="str")
        self.visit_date = LabelAndEntry(self.win, "Visit date", 20, 200, data_type="str")

        self.table = Table(self.win, ["ID", "Patient ID", "Diagnosis", "Treatment plan", "Visit date"],
                           [20, 80, 80, 90, 90], 300, 50, self.select_table)

        Button(self.win, text="New", width=7, command=self.reset_form).place(x=20, y=310)
        Button(self.win, text="Save", width=7, command=self.save_click).place(x=20, y=280)
        Button(self.win, text="Edit", width=7, command=self.edit_click).place(x=90, y=280)
        Button(self.win, text="Remove", width=7, command=self.remove_click).place(x=160, y=280)
        Button(self.win, text="Show Records", width=12, command=self.show_records).place(x=90, y=310)
        Button(self.win, text="Set today", width=7, command=self.set_today, font=("Arial", 8)).place(x=150, y=220)

        self.win.mainloop()

# ui = MedicalRecordView("Medical Record View", "680x370")
