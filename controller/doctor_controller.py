from model.da.da import DataAccess
from model.entity.doctor import Doctor


def save_doctor(name, family, specialization, contact_info):
    try:
        doctor = Doctor(name, family, specialization, contact_info)
        doctor_da = DataAccess(doctor)
        doctor_da.save(doctor)
        return True, doctor.show_doctor_info()
    except Exception as e:
        return False, f"{e}"

def edit_doctor(id ,name, family, specialization, contact_info):
    try:
        doctor = Doctor(name, family, specialization, contact_info)
        doctor.id = id
        doctor_da = DataAccess(doctor)
        doctor_da.edit(doctor)
        return True, doctor.show_doctor_info()
    except Exception as e:
        return False, f"{e}"

def remove_doctor_by_id(id ,name, family, specialization, contact_info):
    try:
        doctor = Doctor(name, family, specialization, contact_info)
        doctor.id = id
        doctor_da = DataAccess(Doctor)
        doctor_da.remove(doctor)
        return True, doctor.show_doctor_info()
    except Exception as e:
        return False, f"{e}"

def find_all_doctors():
    try:
        doctor_da = DataAccess(Doctor)
        all_doctors = doctor_da.find_all()
        return all_doctors
    except Exception as e:
        return False, f"{e}"

def find_doctor_by_id(id):
    try:
        doctor_da = DataAccess(Doctor)
        doctor = doctor_da.find_by_id(id)
        if doctor:
            return True, doctor
        else:
            raise ValueError("doctor not found")
    except Exception as e:
        return False, f"{e}"