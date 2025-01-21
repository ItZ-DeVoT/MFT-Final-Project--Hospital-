from sqlalchemy import Column, Integer, String

from model.entity.base import Base
from model.tools.validation import name_family_validation, number_validation


class Doctor(Base):
    __tablename__ = 'doctors'

    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _name = Column("name",String(30))
    _family = Column("family",String(30))
    _specialization = Column("specialization",String(30))
    _contact_info = Column("contact_info",Integer)

    def __init__(self, name, family, specialization, contact_info):
        self.id = None
        self.name = name
        self.family = family
        self.specialization = specialization
        self.contact_info = contact_info

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = name_family_validation(value, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        self._family = name_family_validation(value, "Invalid Family")

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        self._specialization = name_family_validation(value, "Invalid Specialization")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        self._contact_info = number_validation(value)

    def show_doctor_info(self):
        print("Doctor info :")
        print(f" Name : {self.name}\n Family : {self.family}\n Specialization : {self.specialization}\n Phone : {self.contact_info}")