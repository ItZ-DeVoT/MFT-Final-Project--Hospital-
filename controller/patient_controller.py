from model.da.da import DataAccess
from model.entity.patient import Patient


def save_patient(name, family, age, gender, contact_info, date_of_registration):
    try:
        patient = Patient(name, family, age, gender, contact_info, date_of_registration)
        patient_da = DataAccess(Patient)
        patient_da.save(patient)
        return True, patient.show_patient_info()
    except Exception as e:
        return False, f"{e}"

def edit_patient(id ,name, family, age, gender, contact_info, date_of_registration):
    try:
        patient = Patient(name, family, age, gender, contact_info, date_of_registration)
        patient.id = id
        patient_da = DataAccess(Patient)
        patient_da.edit(patient)
        return True, patient.show_patient_info()
    except Exception as e:
        return False, f"{e}"

def remove_patient_by_id(id, name, family, age, gender, contact_info, date_of_registration):
    try:
        patient = Patient(name, family, age, gender, contact_info, date_of_registration)
        patient.id = id
        patient_da = DataAccess(Patient)
        patient_da.remove(patient)
        return True, patient.show_patient_info()
    except Exception as e:
        return False, f"{e}"

def find_all_patients():
    try:
        patient_da = DataAccess(Patient)
        all_patients = patient_da.find_all()
        return True, all_patients
    except Exception as e:
        return False, f"{e}"

def find_patient_by_id(id):
    try:
        patient_da = DataAccess(Patient)
        patient = patient_da.find_by_id(id)
        if patient:
            return True, patient
        else:
            raise ValueError("Patient not found")
    except Exception as e:
        return False, f"{e}"