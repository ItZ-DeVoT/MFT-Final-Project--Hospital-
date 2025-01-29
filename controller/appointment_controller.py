from model.da.da import DataAccess
from model.entity.appointment import Appointment
from controller.patient_controller import find_patient_by_id
from controller.doctor_controller import find_doctor_by_id


def save_appointment(patient_id, doctor_id, appointment_date, status):
    try:
        appointment = Appointment(patient_id, doctor_id, appointment_date, status)
        appointment_da = DataAccess(appointment)
        patient_info = find_patient_by_id(patient_id)
        doctor_info = find_doctor_by_id(doctor_id)
        if patient_info[0] == True and doctor_info[0] == True:
            appointment_da.save(appointment)
            return True, appointment
        else:
            if patient_info[0] == False:
                return False, "Patient not found"
            if doctor_info[0] == False:
                return False, "Doctor not found"
    except Exception as e:
        return False, f"{e}"

def edit_appointment(id ,patient, doctor, appointment_date, status):
    try:
        appointment = Appointment(patient, doctor, appointment_date, status)
        appointment.id = id
        appointment_da = DataAccess(appointment)
        appointment_da.edit(appointment)
        return True, appointment
    except Exception as e:
        return False, f"{e}"

def remove_appointment_by_id(id ,patient, doctor, appointment_date, status):
    try:
        appointment = Appointment(patient, doctor, appointment_date, status)
        appointment.id = id
        appointment_da = DataAccess(Appointment)
        appointment_da.remove(appointment)
        return True
    except Exception as e:
        return False, f"{e}"

def find_all_appointments():
    try:
        appointment_da = DataAccess(Appointment)
        all_appointments = appointment_da.find_all()
        return all_appointments
    except Exception as e:
        return False, f"{e}"

def find_appointment_by_id(id):
    try:
        appointment_da = DataAccess(Appointment)
        appointment = appointment_da.find_by_id(id)
        if appointment:
            return True, appointment
        else:
            raise ValueError("Appointment not found")
    except Exception as e:
        return False, f"{e}"