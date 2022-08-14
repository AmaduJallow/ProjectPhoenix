class Contact:
    contacts = None

    def __init__(self, ):
        self.contacts = []

    def add_contact(self, name, address, number):
        contact = [name, address, number]
        self.contacts.append(contact)

    def find_contact(self, search_name):
        for contact in self.contacts:
            if search_name.lower().strip() in contact[0].lower().strip():
                print(f"Contact detail: Name: {contact[0]}, address: {contact[1]}, and numbers: {contact[2]} ")
                break
        else:
            print("User does not exist!")

    def find_contact_re(self, search_name):
        position = 0
        for contact in self.contacts:
            if search_name.lower().strip() in contact[0].lower().strip():
                return position
            else:
                position += 1
        else:
            return -1

    def show_contacts(self):
        for contact in self.contacts:
            name, address, number = contact
            print(f"Name: {name} , Address: {address}, Number: {number}")

    def edit_contact(self, search_name):
        position = self.find_contact_re(search_name)
        if position < 0:
            print("Contact does not exit")
        else:
            name = input("Please enter the new name: ")
            address = input("Please enter the new address:")
            numbers = int(input("Please enter the new contact number: "))
            self.contacts[position][0] = name
            self.contacts[position][1] = address
            self.contacts[position][2] = numbers
            print("Edited Successfully")


user = Contact()
user.add_contact("Amadu Jallow", "Brusubi", 2300121)
user.add_contact("Mariama Cham", "LatriKunda", 3707085)
user.add_contact("Abdourahman Jallow","Brusubi", 3266457)
user.add_contact("Sulayman Jallow", "Bufar Zone", 2101211)
