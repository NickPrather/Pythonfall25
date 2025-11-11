"""
Define a Pet Class:
Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
Set a default value for pet_type as "Dog".
Implement getter and setter methods for all properties.
Include a class variable vet_name set to the name of your veterinary office.
Add a method display_pet_info to print all details of the pet and owner.
Create Pet Objects:
Instantiate at least three pet objects with different details.
Show the use of setter methods for at least one pet object.
Implement Property Existence Check:
Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
Display Information:
Use display_pet_info to print details for each pet.
Show three examples of check_property being used on various properties and pets.
show two examples of display_pet_info on different instances of pet that you create

"""
# defines pet as a class
class Pet:
    vet_name = "Nicks Clinic"
# initializes the attributes kept by the vet clinic
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type ="dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
# obtains the owners first name and returns it
    def get_owner_first_name(self):
        return self.__owner_first_name
# obtains owners last name and returns it 
    def get_owner_last_name(self):
        return self.__owner_last_name
# obtains pet id and returns it 
    def get_pet_id(self):
        return self.__pet_id
# obtains pet name and returns it
    def get_pet_name(self):
        return self.__pet_name
# obtains pet type and returns it
    def get_pet_type(self):
        return self.__pet_type
# updates the private attributes for each patient
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name

    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type
# main function that displays the final output
    def main(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Vet: {Pet.vet_name}")
        # spacer line used to make each pets information separated
        print(f"-----------------------------")
# checks property for attribute
def check_property(obj, property_name):
    return hasattr(obj, property_name)
   
# contains each patients info
pet1 = Pet("Alice", "Smith", 296, "Fluffy", "Dog")
pet2 = Pet("Brian", "Gabriel", 245, "Dave", "Cat")
pet3 = Pet("Carla", "Hart", 476, "Bart")
# checks to see if each pet has one of these attributes
check_property(pet1, "_Pet__pet_name")     
check_property(pet2, "_Pet__pet_hair_length")    
check_property(pet3, "_Pet__pet_type")  
# runs each patient under the main function
pet1.main()
pet2.main()
pet3.main()
