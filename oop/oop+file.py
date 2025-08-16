class Contact:
    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

class PhoneBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]

    def list_contacts(self):
        if not self.contacts:
            print("Danh sách trống!")
        else:
            for contact in self.contacts:
                print(contact)
    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for contact in self.contacts:
                f.write(f"{contact.name}, {contact.phone}, {contact.email}\n")
    def load_to_file(self, filename):
        try:
            with open(filename, "r", encoding = "utf-8") as f:
                for line in f:
                    name, phone, email = line.strip().split(",")
                    self.add_contact(Contact(name, phone, email))
        except FileNotFoundError:
            print("Không tồn tại trong danh bạ")

pb = PhoneBook()

pb.load_to_file("contacts.txt")

pb.add_contact(Contact("Nam", "0123456789", "nam@yahoo.com"))
pb.add_contact(Contact("Luong", "0814299304","vul45845@gmail.com"))

pb.list_contacts()

pb.save_to_file("contacts.txt")

# Xóa liên hệ và in lại
pb.remove_contact("Nam")
print("\nSau khi xóa:")
pb.list_contacts()

