from colorama import Fore,Style,init
init(autoreset=True) # for reset the color in new element

def IBW():
    """
        calculate the ideal body weight base on this formola :
        Male IBW => 50 kg + 2.3 kg * (height(inch) - 60)
        Female IBW => 45.5 kg + 2.3 kg * (height(inch) - 60)
    """
    pass

def BMI():
    """
        Body Mass Index is a standard to determine your
        health situation. the formola is :
        BMI => weight (kg) / height (m) * height (m)
    """
    pass

if __name__ == "__main__":
    print(Fore.LIGHTGREEN_EX+"Welcome to ideal body calculator!"+"\n"+"Please answer these questions :")
    gender = input("What is your gender ? ( Male(m) / Female(m) ) : ")
    height = float(input("How much do you height ? (cm) :"))
    weight = int(input("How much do you weight ? (Kg) :"))