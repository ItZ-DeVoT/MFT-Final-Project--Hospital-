from model.da.da import DataAccess
from model.entity.medical_record import MedicalRecord
from controller.patient_controller import find_patient_by_id


def save_record(patient_id, diagnosis, treatment_plan, visit_date):
    try:
        medical_record = MedicalRecord(patient_id, diagnosis, treatment_plan, visit_date)
        medical_da = DataAccess(medical_record)
        patient_info = find_patient_by_id(patient_id)
        if patient_info[0] == True:
            medical_da.save(medical_record)
            return True, medical_record
        else:
            return False, "Patient not found"
    except Exception as e:
        return False, f"{e}"


def edit_record(id, patient, diagnosis, treatment_plan, visit_date):
    try:
        medical_record = MedicalRecord(patient, diagnosis, treatment_plan, visit_date)
        medical_record.id = id
        medical_record_da = DataAccess(medical_record)
        medical_record_da.edit(medical_record)
        return True
    except Exception as e:
        return False, f"{e}"


def remove_medical_record_by_id(id, patient, diagnosis, treatment_plan, visit_date):
    try:
        medical_record = MedicalRecord(patient, diagnosis, treatment_plan, visit_date)
        medical_record.id = id
        medical_record_da = DataAccess(MedicalRecord)
        medical_record_da.remove(medical_record)
        return True
    except Exception as e:
        return False, f"{e}"


def find_all_medical_records():
    try:
        medical_record_da = DataAccess(MedicalRecord)
        all_medical_records = medical_record_da.find_all()
        print(all_medical_records)
        return all_medical_records
    except Exception as e:
        return False, f"{e}"


def find_medical_record_by_id(id):
    try:
        medical_record_da = DataAccess(MedicalRecord)
        medical_record = medical_record_da.find_by_id(id)
        if medical_record:
            return True, medical_record
        else:
            raise ValueError("Medical Record not found")
    except Exception as e:
        return False, f"{e}"