from tkinter import *

from view.appointment_view import AppointmentView
from view.medical_record_view import MedicalRecordView
from view.patient_view import PatientView
from view.doctor_view import DoctorView


def main_app():
    PatientView("Patient View", "740x380", open_doctors_command=open_doctors, open_records_command=open_records,
            open_appointments_command=open_appointments)

def open_doctors(current_view):
    current_view.destroy_window()
    DoctorView("Doctor View", "620x370")
    main_app()


def open_records(current_view):
    current_view.destroy_window()
    MedicalRecordView("Medical Record View", "680x370")
    main_app()

def open_appointments(current_view):
    current_view.destroy_window()
    AppointmentView("Appointment View", "710x380")
    main_app()


main_app()
