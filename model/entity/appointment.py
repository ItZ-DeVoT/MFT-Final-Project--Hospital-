from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from model.entity.base import Base


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column("id" ,Integer, primary_key=True, autoincrement=True)
    patient_id = Column("patient_id" ,Integer, ForeignKey('patients.id'))
    doctor_id = Column("doctor_id" ,Integer, ForeignKey('doctors.id'))
    appointment_date = Column("appointment_date" ,Date)
    status = Column("status" ,String(30))

    patient = relationship("Patient")
    doctor = relationship("Doctor")

    def __init__(self, patient, doctor, appointment_date, status):
        self.id = None
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.status = status
