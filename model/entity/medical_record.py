from sqlalchemy import Integer, Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.tools.validation import name_family_validation, date_validation


class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _patient_id = Column("patient_id", Integer, ForeignKey('patients.id'))
    _diagnosis = Column("diagnosis", String(40))
    _treatment_plan = Column("treatment_plan", String(40))
    _visit_date = Column("visit_date", Date)

    patient = relationship("Patient")

    def __init__(self, patient_id, diagnosis, treatment_plan, visit_date):
        self.id = None
        self.patient_id = patient_id
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan
        self.visit_date = visit_date

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
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = name_family_validation(value, "Invalid diagnosis")

    @property
    def treatment_plan(self):
        return self._treatment_plan

    @treatment_plan.setter
    def treatment_plan(self, value):
        self._treatment_plan = name_family_validation(value, "Invalid treatment plan")

    @property
    def visit_date(self):
        return self._visit_date

    @visit_date.setter
    def visit_date(self, value):
        self._visit_date = date_validation(value)