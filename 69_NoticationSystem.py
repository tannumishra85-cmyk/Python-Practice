class Email:
    def __init__(self,mail_id):
        self.mail_id = mail_id
        
    def send(self):
        print("Sending Email to", self.mail_id)

class SMS:
    def __init__(self,ph_no):
        self.ph_no = ph_no

    def send(self):
        print("Sending SMS to", self.ph_no)

class WhatsApp:
    def __init__(self, name):
        self.name = name

    def send(self):
        print("Sending WhatsApp to",self.name)


notification = [Email("tannu@gmail.com"),SMS("9876543210"),WhatsApp("Tannu") ]  # Duck typing in python
for msg in notification:
    msg.send()
