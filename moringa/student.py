#Class student with inheritance
from .users import User

class Student(User):
    def __init__(self,name,email,phone,student_email):
        super().__init__(name,email,phone)
        self.student_email = student_email
    
    def send_attendance_warning(self):
        print(f'{self.name} you have been warned')