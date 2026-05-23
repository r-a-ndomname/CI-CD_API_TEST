import json
from dataclasses import dataclass, asdict 

@dataclass
class Student:
    name: str
    location:str
    phone:str
    courses:list

student = Student("Supriti", "Japan", "12469", ["Python", "Java"])
print(student.__dict__)
print(type(student.__dict__))