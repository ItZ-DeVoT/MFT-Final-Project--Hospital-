from sqlalchemy import Integer, Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from model.entity.base import Base


class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patient_records.id'))
    diagnosis = Column(String(40))
    treatment_plan = Column(String(40))
    visit_date = Column(Date)

    patient = relationship("Patient")

    def __init__(self, patient, diagnosis, treatment_plan, visit_date):
        self.patient = patient
        self.diagnosis = diagnosis
        self.treatment_plan = treatment_plan
        self.visit_date = visit_date