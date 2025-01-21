from datetime import date

from model.entity.appointment import Appointment
from model.entity.doctor import Doctor
from model.entity.patient import Patient

patient = Patient("Arshia", "Fadaie", "21", "male",981442567 ,"2025-1-20")
doctor = Doctor("Arshia", "Fadaie", "Computer Science", 981442567)

appointment = Appointment(patient, doctor, date.today(), "DONE")
