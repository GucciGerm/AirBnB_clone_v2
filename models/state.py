#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              backref="State", cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            '''
            This script will get all the City values

            '''
            city = []
            listofcities = models.storage.all("City").values()

            for cit in listofcities:
                if cit.state_id == self.id:
                    city.append(cit)
            return city
