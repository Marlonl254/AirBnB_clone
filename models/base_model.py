#!/usr/bin/python3
'''
The Base Model of the Project
'''

from datetime import datetime
import uuid

class BaseModel:
    '''This is the base Model Of our project from which Feature Classes are derrived'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        
    def __str__(self):
        '''String representation of the base model class'''
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) <{self.__dict__}>"
    
    def save(self):
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

obj = BaseModel()

print(obj.to_dict())