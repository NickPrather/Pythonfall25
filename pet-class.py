"""

Submit the Python script containing the Pet class definition and instances 
by uploading it to your GitHub repository and submitting the link
Include comments to demonstrate the usage of the chosen special method or function.
Ensure code follows Python best practices for readability and efficiency.


"""
# defines Pet as the class
class Pet:
   # initializes the attributes  
    def __init__(self, kind, breed, name):
        self.kind = kind 
        self.breed = breed
        self.name = name
# get functions to obtain the attributes
    def get_kind(self):
        return self.kind

   
    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name
# set functions to set the attributes   
    def set_breed(self, breed):
        self.breed = breed

    def set_name(self, name):
        self.name = name
        
    def set_kind(self, kind):
            self.kind = kind
# prints out the attributes for the 3 different Pets in a organized manor   
    def print(self):
         print(f"name: {self.name}")
         print(f"kind: {self.kind}")
         print(f"breed: {self.breed}")
         print(f"---------------------") # spacer line added for clarity
# pet attributes 
pet1 = Pet("Dog", "Labrador", "steve")
pet2 = Pet("Cat", "RagDoll", "Chuck")
pet3 = Pet("Cat", "Mainecoon", "Megatron")      
# runs the program
pet1.print()
pet2.print()
pet3.print()

# type() shows the class used to represent the object
print(type(pet1))

# isinstance()  checks if an object is an instance of the class
print(isinstance(pet2, Pet))  # Expected to output true
print(isinstance(pet3, str))  # Expected to output false

# __module__ returns the module name in which the pet class is defined
print(Pet.__module__)  
