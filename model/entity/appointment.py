from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.tools.validation import date_validation


class Appointment(Base):
    __tablename__ = 'appointments'

    _id = Column("id" ,Integer, primary_key=True, autoincrement=True)
    _patient_id = Column("patient_id" ,Integer, ForeignKey('patients.id'))
    _doctor_id = Column("doctor_id" ,Integer, ForeignKey('doctors.id'))
    _appointment_date = Column("appointment_date" ,Date)
    status = Column(String(30))

    patient = relationship("Patient")
    doctor = relationship("Doctor")

    def __init__(self, patient_id, doctor_id, appointment_date, status):
        self.id = None
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        if type(value) == int:
            self._patient_id = value
        else:
            raise ValueError("Patient ID must be a number")

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        if type(value) == int:
            self._doctor_id = value
        else:
            raise ValueError("Doctor ID must be a number")

    @property
    def appointment_date(self):
        return self._appointment_date

    @appointment_date.setter
    def appointment_date(self, value):
        self._appointment_date = date_validation(value)