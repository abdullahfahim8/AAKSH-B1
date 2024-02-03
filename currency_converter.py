#Simple Currency Converter

def SARTOBDT(sar):
    tk = sar * 32.5
    print(tk)

def BDTTOSAR(tk):
    sar = tk/32.5
    print(sar)

def Eurtobdt(eur):
    tk = eur * 119.46
    print(tk)

def bdttoeur(tk):
    euro = tk/119.46
    print(euro)

def Usdtobdt(Usd):
    tk = Usd * 109.6
    print(tk)

def bdttousd(tk):
    Usd = tk/109.6
    print(Usd)

while True:
    print("Currency Converter!\n1.Saudi Rial To BDT\n2.BDT To Saudi Rial\n3.Euro To BDT")
    print("4.BDT To Euro\n5.USD To BDT\n6.BDT to USD\n7.Exit!")


    choice = int(input("Enter Your Choice ,Please !\n"))

    if choice == 1:
        sar = float(input("Enter Saudi Rial:"))
        SARTOBDT(sar)

    elif choice == 2:
        tk = float(input("Enter BDT:"))
        BDTTOSAR(tk)

    elif choice == 3:
        eur = float(input("Enter EURO:"))
        Eurtobdt(eur)

    elif choice ==4:
        tk=float(input("enter BDT:"))
        bdttoeur(tk)
    elif choice ==5:
        Usd = float(input("enter usd:"))
        Usdtobdt(Usd)
    elif choice ==6:
        tk =float(input("enter BDT:"))
        bdttousd(tk)
    elif choice==7:
        print("Thanks for using our system")
        break
    else:
        print("you entered a wrong choice! Enter correctly")


"""Created By AAKHS B1! 
Jannat, Nijhum , Nusrat , Prity  , Tisha , Tasbah , Tajrin , Faria"""
