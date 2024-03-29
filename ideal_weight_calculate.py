from colorama import Fore, Style, init
import traceback
init(autoreset=True)  # for reset the color in new element


logo = """
  _____    _            _ __    __     _       _     _   
  \_   \__| | ___  __ _| / / /\ \ \___(_) __ _| |__ | |_ 
   / /\/ _` |/ _ \/ _` | \ \/  \/ / _ \ |/ _` | '_ \| __|
/\/ /_| (_| |  __/ (_| | |\  /\  /  __/ | (_| | | | | |_ 
\____/ \__,_|\___|\__,_|_| \/  \/ \___|_|\__, |_| |_|\__|
                                         |___/           
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+ Made By : mehran.safaripour@gmail.com                 +
+           arezoo.darvish6969@gmail.com                +
+                                                       +
+ Welcome to ideal body calculator !                    +
+ Please answer these questions :                       +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


def ibw(height , gender):
    """
        calculate the ideal body weight base on this formola :
        Male IBW => 50 kg + 2.3 kg * (height(inch) - 60)
        Female IBW => 45.5 kg + 2.3 kg * (height(inch) - 60)
    """
    try:
        #1 cm ==> 0.3937007874 inch
        index = 0.3937007874
        if gender == 1:  # male
            ideal_weight = 50 + (2.3*((height*index)-60))
        else:
            ideal_weight = 45.5 + (2.3*((height*index)-60))
        return round(ideal_weight)
    except:
        print(traceback.format_exc)
        return "Something Wrong!"



def bmi(weight, height):
    """
        Body Mass Index is a standard to determine your
        health situation. the formola is :
        BMI => weight (kg) / height (m) * height (m)
    """
    try:
        situation = ''
        bmi = weight / (height * height)
        if bmi < 19:
            situation = "Underweight. You need to add some weight!"
        elif bmi >= 19 and bmi < 25:
            situation = "Injustice. Exellent keep it on."
        elif bmi >= 25 and bmi < 30:
            situation = "Overweight. If you want to be healthy you need to lose weight!"
        elif bmi >= 30:
            situation = "Chubby!. Soon you will be die :)"
        return situation
    except:
        print(traceback.format_exc())
        return "something Wrong!"


if __name__ == "__main__":
    print(Fore.LIGHTGREEN_EX + logo)
    # inputs
    gender = int(input("What is your gender ? ( Male(1) / Female(2) ) : "))
    height = float(input("How much do you height ? (cm) : "))
    weight = float(input("How much do you weight ? (Kg) : "))
    # Body Mass Index calculator
    print(Fore.LIGHTYELLOW_EX + "\nBody Mass Index : " + Style.BRIGHT + bmi(weight,( height / 100)))
    # ideal body weight calculator
    print(Fore.LIGHTRED_EX + "Ideal Weight : " + Style.BRIGHT + str(ibw(height, gender)))
