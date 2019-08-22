from colorama import Fore, Style, init
import traceback
init(autoreset=True)  # for reset the color in new element


def ibw():
    """
        calculate the ideal body weight base on this formola :
        Male IBW => 50 kg + 2.3 kg * (height(inch) - 60)
        Female IBW => 45.5 kg + 2.3 kg * (height(inch) - 60)
    """
    pass


def bmi(weight, height):
    """
        Body Mass Index is a standard to determine your
        health situation. the formola is :
        BMI => weight (kg) / height (m) * height (m)
    """
    try:
        type = ''
        bmi = weight / (height * height)
        print(bmi)
        if bmi < 19:
            type = "کمبود وزن"
        elif bmi >= 19 and bmi < 25:
            type = "مطلوب"
        elif bmi >= 25 and bmi < 30:
            type = "اضافه وزن"
        elif bmi >= 30:
            type = "چاق"
        return type
    except:
        print(traceback.format_exc())
        return []


if __name__ == "__main__":
    print(Fore.LIGHTGREEN_EX + "Welcome to ideal body calculator!" + "\n" + "Please answer these questions :")
    gender = input("What is your gender ? ( Male(m) / Female(m) ) : ")
    height = float(input("How much do you height ? (cm) :"))
    weight = int(input("How much do you weight ? (Kg) :"))
    bmi = print("شرایط بدنی : " + str(bmi(weight,( height / 100))))
