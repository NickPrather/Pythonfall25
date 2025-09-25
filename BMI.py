"""
Create a BMI calculator that takes a user's weight and height,
 calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.
"""
# function that asks for user input and then calculates BMI and categorizes it
def BMI_calculator():
        weight = float(input("enter your weight in pounds: "))
        height = float(input("enter your height in inches: "))
        weight_kg = weight * 0.453592
        height_m = height * 0.0254
        bmi = weight_kg / (height_m ** 2)
        print(f"your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            print ("you are underweight")
        elif 18.5 <= bmi < 24.9:
            print("you are normal weight")
        elif 25 <= bmi < 29.9:
            print("you are overweight")
        elif bmi >= 30:
            print("you are obese")
        return bmi
# main function that runs the program
def main():
    BMI_calculator()
# run the main function
main()
