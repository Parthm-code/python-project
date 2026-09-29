








def water_intake_calculator():
    usr_inp1=float(input("Enter your water intake in liters: "))
    if usr_inp1<2:
        print("You need to drink more water")
    elif usr_inp1>=2 and usr_inp1<=3:    
        print("You are drinking an adequate amount of water")


def bmi_calculator():
    usr_inp1=float(input("Enter your weight in kg: "))
    usr_inp2=float(input("Enter your height in meters: "))
    usr_bmi=usr_inp1/(usr_inp2**2)
    try:
        if usr_bmi<18.5:
            print("You are underweight")
        elif usr_bmi>=18.5 and usr_bmi<=24.9:
            print("You are healthy")
        elif usr_bmi>24.9:
            print("You are overweight")
    except ZeroDivisionError:
        print("Height cannot be zero.")
    print(f"Your BMI is: {usr_bmi:.2f}")   


def exercisetime():
    usr_inp1=int(input("Enter your exercise time in minutes: "))
    if usr_inp1<30:
        print("You need to exercise more")
    elif usr_inp1>=30 and usr_inp1<=60:
        print("You are exercising an right amount")
    elif usr_inp1>60:
        print("You are exercising too much, please be careful not to overdo it!")

def sleepcal():
    try:
        slp=float(input("enter your daily sleep in hours"))
        if slp < 0:
            print("Sleep hours cannot be negative.")
        elif slp < 7:
            print("You should try to get more sleep.")
        elif slp <= 9:
            print("Your sleep duration is in a good range.")
        else:
            print("You may be sleeping more than necessary.")
        
        return slp
        
    except ValueError:
            print("Please enter a valid number.")
            return 0
        
def caloriecal():
    try:
        wt = float(input("Enter your weight in kg: "))
        ht = float(input("Enter your height in cm: "))
        age = int(input("Enter your age: "))

        if wt <= 0 or ht <= 0 or age <= 0:
            print("All values must be greater than zero.")
            return

        print("\nSelect your activity level:")
        print("1. Sedentary")
        print("2. Lightly active")
        print("3. Moderately active")
        print("4. Very active")

        activity = input("Enter your choice: ")

        # Basic BMR calculation
        bmr = (10 * wt) + (6.25 * ht) - (5 * age) + 5

        if activity == "1":
            calories = bmr * 1.2
        elif activity == "2":
            calories = bmr * 1.375
        elif activity == "3":
            calories = bmr * 1.55
        elif activity == "4":
            calories = bmr * 1.725
        else:
            print("Invalid activity level.")
            return

        print(f"Estimated daily calorie requirement: {calories:.0f} calories")

    except ValueError:
        print("Please enter valid numbers.")


def health_report():
    print("\n******** HEALTH REPORT ********")

    water = float(input("Enter your water intake in liters: "))
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    exercise = int(input("Enter your exercise time in minutes: "))
    sleep = float(input("Enter your sleep in hours: "))

    score = 0

    if 2 <= water <= 3:
        score += 25

    bmi = weight / (height ** 2)

    if 18.5 <= bmi <= 24.9:
        score += 25

    if 30 <= exercise <= 60:
        score += 25

    if 7 <= sleep <= 9:
        score += 25

    print(f"\nBMI: {bmi:.2f}")
    print(f"Health Score: {score}/100")

    if score >= 75:
        print("Your overall health habits look good.")
    elif score >= 50:
        print("Your health habits are decent, but there is room for improvement.")
    else:
        print("You should focus on improving your daily health habits.")

    print("********************************")

    




print("********Welcome to the Health Calculator********")
print("Please select an option:")
print("1: Calculate Water Intake\n2: Calculate BMI\n3: Calculate Exercise Time\n4: sleep calculator\n5:calorie calculator\n6:Health report\n7:exit")

while True:
    choice = input("Enter your choice (1/2/3/4/5/6/7):")
    if choice == "1":
        water_intake_calculator()
    elif choice == "2":
        bmi_calculator()
    elif choice == "3":
        exercisetime()
    elif choice == "4":
         sleepcal() 
    elif choice == "5":
        caloriecal()
    elif choice == "6":
        health_report()

   
   
    elif choice == "7":
        print("******Exiting the program. Stay healthy!******")
        break
    else:
        print("Invalid choice. Please try again.")
        

        






