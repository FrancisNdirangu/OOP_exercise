class User:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def send_message(self):
        print(f'hello {self.name}')
