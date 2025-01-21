from sqlalchemy import String, Integer, Column, Date
from model.entity.base import Base
from model.tools.validation import *


class Patient(Base):
    __tablename__ = 'patients'

    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _name = Column("name",String(30))
    _family = Column("family",String(30))
    _age = Column("age",Integer)
    _gender = Column("gender",String(30))
    _contact_info = Column("contact_info",Integer)
    _date_of_registration = Column("date_of_registration",Date)

    def __init__(self, name, family, age, gender,contact_info, date_of_registration):
        self.id = None
        self.name = name
        self.family = family
        self.age = age
        self.gender = gender
        self.contact_info = contact_info
        self.date_of_registration = date_of_registration

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
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if type(value) == str and re.match("\d", value):
            value = int(value)
            if 1 <= value <= 90:
                self._age = value
            else:
                raise ValueError("Age must be between 1 and 90")
        else:
            raise ValueError("Age must be a number!")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = gender_validation(value)

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        self._contact_info = number_validation(value)

    @property
    def date_of_registration(self):
        return self._date_of_registration

    @date_of_registration.setter
    def date_of_registration(self, value):
        self._date_of_registration = date_validation(value)

    def show_patient_info(self):
        print("Patient info :")
        print(f" Name : {self.name}\n Family : {self.family}\n Age : {self.age}\n Gender : {self.gender}\n Phone : {self.contact_info}\n Registration Date : {self.date_of_registration}")