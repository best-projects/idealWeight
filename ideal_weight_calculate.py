from colorama import Fore,Style,init
init(autoreset=True)

def IBW():
    pass

def BMI():
    pass

if __name__ == "__main__":
    print(Fore.LIGHTGREEN_EX+"Welcome to ideal body calculator!"+"\n"+"Please answer these questions :")
    gender = input("What is your gender ? ( Male(m) / Female(m) ) : ")
    height =float(input("how much do you height ? (cm) "))