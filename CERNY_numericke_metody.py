##from numpy import sin, cos, tan, cosh, tanh, sinh
import math
def menu():
    print("\n")
    print("[1] ZAPIS VLASTNI FUNKCE")
    print("\n")
    print("Preddefinovane funkce:")
    print("[2] a*sin(b*x)")
    print("[3] a*cos(b*x)")
    print("[4] a*x**3+c")
    print("[5] a*x**2 + b*x + c")
    print("\n")
def podmenu():
    print("[1] Metoda bisekce")
    print("[2] Metoda secen")
    print("[3] Metoda kroku")
    print("[0] ZPET")
    print("\n")

def bisection(w, a, b, d):  ##w...funkce, ab rozmezí, d... přesnost

    def f(x):
        f = eval(w)
        return f
    error = abs(b - a)

    while error > d:
        c = (b + a) / 2
        
        if f(a) * f(b) >= 0: ##overeni pritomnosti nejakeho korenu v rozmezi
            print(f"Zadny, nebo vice korenu, zkus zadat jine rozmezi, jinou metodu, nez bisekci!")
            quit()
        elif f(c) * f(a) < 0: ## na techto dvou elif overujeme, jestli je koren v leve, ci v prave casti grafu
            b = c
            error = abs(b - a)
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)
        else:
            print("Neco neni v poradku. Zkus znovu zadat funkci.")
            quit()
    print(f"Odchylka vysledku je {error}")
    print(f"Spodni hranice, ve ktere se nachazi koren, je {a} a horni hranice je {b}")       
    print('\nPozadovany koren je: %0.6f' % ((a+b)/2))
    


    
def krok(w, a, b, d): ##w...funkce, ab...rozmezi, d...presnost

    def f(x):
        f = eval(w)
        return f
    error = abs(b - a)
    x1 = a
    x2 = a + d
    pocetkorenu = 0
    while x1 < b:
        if f(x1) * f(x2) < 0:
            print(f"Jeden z korenu se nachazi mezi {x1} a {x2}")
            print('\nPozadovany koren je priblizne: %0.5f' % ((x1+x2)/2))
            pocetkorenu = pocetkorenu + 1
        x1 = x1 + d
        x2 = x2 + d
    print(f"Celkem program nalezl {pocetkorenu} Korenu. Vypsane jsou vyse.")
    
def secny(w, x1, x2, d):
    def f(x):
        f = eval(w)
        return f
     
    podminka = True
    kroky = 1
    while podminka:
        if f(x1) == f(x2):
            print("Deleni nulou, vyber jine pocatecni body!")
            quit()

        x3 = x1 - (x2-x1)*f(x1)/(f(x2) - f(x1) )
        print("Iterace-%d, x3 = %0.6f a f(x3) = %0.6f" % (kroky, x3, f(x3)))
        x1 = x2
        x2 = x3
        kroky = kroky + 1

        podminka = abs(f(x2)) > d
    print('\n Pozadovany koren je: %0.6f' % x3)
        


vyb = 5

while vyb != 0:
    print("\n")
    print("\n")
    print(f"Vitej v programu k reseni nelinearnich rovnic pomoci metod secen, bisekce a kroku.")
    menu()
    vyb = input("Zadej cislo: ")
    vyb = int(vyb)
    if vyb == 1:
        print(f"Vybral jsi {vyb}")
        print(f"Zapis vlastni funkce\n")
        podmenu()
        podvyb = input("Jakou metodu chces pouzit:  ")
        podvyb = int(podvyb)
        if podvyb == 1:
            print(f"Vybral jsi metodu bisekce")
            rovnice = input("Zadej rovnici v libovolnem tvaru (priklad... -3*x*x + 6)\nNepouzivej ale goniometricke funkce: ")
            ##koefa = float(koefa) neni potreba, vyraz chceme jako string aby ho funkce eval mohla prevest.
            rozma = input("Zadej minimum:  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej maximum:  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            bisection(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 2:
            print(f"Vybral jsi metodu secen")
            rovnice = input("Zadej rovnici v libovolnem tvaru (priklad... -3*x*x + 6)\nNepouzivej ale goniometricke funkce: ")
            rozma = input("Zadej prvni hodnotu secny (x1):  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej druhou hodnotu secny (x2):  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            secny(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 3:
            print(f"Vybral jsi {vyb}\n")
            print(f"Vybral jsi metodu kroku")

            rovnicek = input("Zadej rovnici v libovolnem tvaru (priklad... -3*x*x + 6)\nNepouzivej ale goniometricke funkce: ")
            rozmak = input("Zadej minimum:  ")
            if isinstance(rozmak, str):
                rozmak = float(rozmak)
            rozmbk = input("Zadej maximum:  ")
            if isinstance(rozmbk, str):
                rozmbk = float(rozmbk)
            presnostk = input("Zadej presnost hledani:  ")
            if isinstance(presnostk, str):
                presnostk = float(presnostk)
            krok(rovnicek, rozmak, rozmbk, presnostk)
            
       
        elif podvyb == 0:
            print("Vracim se do hlavniho menu...")










    elif vyb == 2:
        print(f"Vybral jsi {vyb}")
        print(f"Vybral jsi a*sin(b*x)\n")
        
        podmenu()
        podvyb = input("Jakou metodu chces pouzit:  ")
        podvyb = int(podvyb)
        if podvyb == 1:
            print(f"Vybral jsi metodu bisekce")

            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")
            ##if isinstance(koefa, str):
              ##  koefa = float(koefa)
            star = "*"
            koefa = koefa + star
            rovnice = "math.sin("
            rovnice = koefa + rovnice + koefb
            addon = "*x)"
            rovnice = rovnice + addon
            print(rovnice)
            ##rovnice = input("Zadej rovnici v libovolnem tvaru (priklad... -3*x*x + 6)\nNepouzivej ale goniometricke funkce: ")
            ##koefa = float(koefa) neni potreba, vyraz chceme jako string aby ho funkce eval mohla prevest.
            rozma = input("Zadej minimum:  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej maximum:  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            bisection(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 2:
            print(f"Vybral jsi metodu secen")
            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")
            ##if isinstance(koefa, str):
              ##  koefa = float(koefa)
            star = "*"
            koefa = koefa + star
            rovnice = "math.sin("
            rovnice = koefa + rovnice + koefb
            addon = "*x)"
            rovnice = rovnice + addon
            print(rovnice)
            rozma = input("Zadej prvni hodnotu secny (x1):  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej druhou hodnotu secny (x2):  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            secny(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 3:
            print(f"Vybral jsi {vyb}\n")
            print(f"Vybral jsi metodu kroku")
            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")
            ##if isinstance(koefa, str):
              ##  koefa = float(koefa)
            star = "*"
            koefa = koefa + star
            rovnice = "math.sin("
            rovnice = koefa + rovnice + koefb
            addon = "*x)"
            rovnice = rovnice + addon
            print(rovnice)
            
            rozmak = input("Zadej minimum:  ")
            if isinstance(rozmak, str):
                rozmak = float(rozmak)
            rozmbk = input("Zadej maximum:  ")
            if isinstance(rozmbk, str):
                rozmbk = float(rozmbk)
            presnostk = input("Zadej presnost hledani:  ")
            if isinstance(presnostk, str):
                presnostk = float(presnostk)
            krok(rovnice, rozmak, rozmbk, presnostk)





        
        
        
    elif vyb == 3:
        print(f"Vybral jsi {vyb}")
        print(f"Vybral jsi a*cos(b*x)\n")
        podmenu()
        podvyb = input("Jakou metodu chces pouzit:  ")
        podvyb = int(podvyb)
        if podvyb == 1:
            print(f"Vybral jsi metodu bisekce")

            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")
            ##if isinstance(koefa, str):
              ##  koefa = float(koefa)
            star = "*"
            koefa = koefa + star
            rovnice = "math.cos("
            rovnice = koefa + rovnice + koefb
            addon = "*x)"
            rovnice = rovnice + addon
            print(rovnice)
            ##rovnice = input("Zadej rovnici v libovolnem tvaru (priklad... -3*x*x + 6)\nNepouzivej ale goniometricke funkce: ")
            ##koefa = float(koefa) neni potreba, vyraz chceme jako string aby ho funkce eval mohla prevest.
            rozma = input("Zadej minimum:  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej maximum:  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            bisection(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 2:
            print(f"Vybral jsi metodu secen")
            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")
            ##if isinstance(koefa, str):
              ##  koefa = float(koefa)
            star = "*"
            koefa = koefa + star
            rovnice = "math.cos("
            rovnice = koefa + rovnice + koefb
            addon = "*x)"
            rovnice = rovnice + addon
            print(rovnice)
            rozma = input("Zadej prvni hodnotu secny (x1):  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej druhou hodnotu secny (x2):  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            secny(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 3:
            print(f"Vybral jsi {vyb}\n")
            print(f"Vybral jsi metodu kroku")
            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")
            ##if isinstance(koefa, str):
              ##  koefa = float(koefa)
            star = "*"
            koefa = koefa + star
            rovnice = "math.cos("
            rovnice = koefa + rovnice + koefb
            addon = "*x)"
            rovnice = rovnice + addon
            print(rovnice)
            
            rozmak = input("Zadej minimum:  ")
            if isinstance(rozmak, str):
                rozmak = float(rozmak)
            rozmbk = input("Zadej maximum:  ")
            if isinstance(rozmbk, str):
                rozmbk = float(rozmbk)
            presnostk = input("Zadej presnost hledani:  ")
            if isinstance(presnostk, str):
                presnostk = float(presnostk)
            krok(rovnice, rozmak, rozmbk, presnostk)







        
    elif vyb == 4:
        print(f"Vybral jsi {vyb}")
        print(f"Vybral jsi a*x**3 + c\n")

        podmenu()
        podvyb = input("Jakou metodu chces pouzit:  ")
        podvyb = int(podvyb)
        if podvyb == 1:
            print(f"Vybral jsi metodu bisekce")

            koefa = input("Zadej koeficient a:  ")
            
            koefc = input("Zadej c:  ")
            star = "*"
            koefa = koefa + star
            rovnice = "x**3 + "
            rovnice = koefa + rovnice + koefc
            print(rovnice)
            
            rozma = input("Zadej minimum:  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej maximum:  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            bisection(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 2:
            print(f"Vybral jsi metodu secen")
            koefa = input("Zadej koeficient a:  ")
            
            koefc = input("Zadej c:  ")
            star = "*"
            koefa = koefa + star
            rovnice = "x**3 + "
            rovnice = koefa + rovnice + koefc
            print(rovnice)
            rozma = input("Zadej prvni hodnotu secny (x1):  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej druhou hodnotu secny (x2):  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            secny(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 3:
            print(f"Vybral jsi {vyb}\n")
            print(f"Vybral jsi metodu kroku")
            koefa = input("Zadej koeficient a:  ")
            
            koefc = input("Zadej c:  ")
            star = "*"
            koefa = koefa + star
            rovnice = "x**3 + "
            rovnice = koefa + rovnice + koefc
            print(rovnice)
            
            rozmak = input("Zadej minimum:  ")
            if isinstance(rozmak, str):
                rozmak = float(rozmak)
            rozmbk = input("Zadej maximum:  ")
            if isinstance(rozmbk, str):
                rozmbk = float(rozmbk)
            presnostk = input("Zadej presnost hledani:  ")
            if isinstance(presnostk, str):
                presnostk = float(presnostk)
            krok(rovnice, rozmak, rozmbk, presnostk)


        


        
    elif vyb == 5:
        print(f"Vybral jsi {vyb}")
        print(f"Vybral jsi a*x**2 + b*x + c\n")
        
        podmenu()
        podvyb = input("Jakou metodu chces pouzit:  ")
        podvyb = int(podvyb)
        if podvyb == 1:
            print(f"Vybral jsi metodu bisekce")

            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")

            koefc = input("Zadej c (zadej vcetne znamenka +, nebo -:  ")
            star = "*"
            koefa = koefa + star
            rovnice = "x**2 + "
            dopln = "*x "
            koefb = koefb + dopln
            rovnice = koefa + rovnice + koefb + koefc
            print(rovnice)
            
            rozma = input("Zadej minimum:  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej maximum:  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            bisection(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 2:
            print(f"Vybral jsi metodu secen")
            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")

            koefc = input("Zadej c (zadej vcetne znamenka +, nebo -:  ")
            star = "*"
            koefa = koefa + star
            rovnice = "x**2 + "
            dopln = "*x "
            koefb = koefb + dopln
            rovnice = koefa + rovnice + koefb + koefc
            print(rovnice)
            rozma = input("Zadej prvni hodnotu secny (x1):  ")
            if isinstance(rozma, str):
                rozma = float(rozma)
            rozmb = input("Zadej druhou hodnotu secny (x2):  ")
            if isinstance(rozmb, str):
                rozmb = float(rozmb)
            presnost = input("Zadej presnost hledani:  ")
            if isinstance(presnost, str):
                presnost = float(presnost)
            secny(rovnice, rozma, rozmb, presnost)
            
        elif podvyb == 3:
            print(f"Vybral jsi {vyb}\n")
            print(f"Vybral jsi metodu kroku")
            koefa = input("Zadej koeficient a:  ")
            
            koefb = input("Zadej koeficient b:  ")

            koefc = input("Zadej c (zadej vcetne znamenka +, nebo -:  ")
            star = "*"
            koefa = koefa + star
            rovnice = "x**2 + "
            dopln = "*x "
            koefb = koefb + dopln
            rovnice = koefa + rovnice + koefb + koefc
            print(rovnice)
            
            rozmak = input("Zadej minimum:  ")
            if isinstance(rozmak, str):
                rozmak = float(rozmak)
            rozmbk = input("Zadej maximum:  ")
            if isinstance(rozmbk, str):
                rozmbk = float(rozmbk)
            presnostk = input("Zadej presnost hledani:  ")
            if isinstance(presnostk, str):
                presnostk = float(presnostk)
            krok(rovnice, rozmak, rozmbk, presnostk)







    elif vyb == 0:
        print(f"Diky za vyuziti programu.")
    else:
        print(f"vybral jsi nespravne cislo!")
              

