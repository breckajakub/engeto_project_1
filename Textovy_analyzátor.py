'''
author = Jakub Břečka
'''
text1 = '''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive . 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. '''
text1_split = text1.split()
vyčištěný_text1 = []
for slovo in text1_split:
    vyčištěný_text1.append(slovo.strip(".,:;"))
for slovo in vyčištěný_text1:
  if slovo == "":
    vyčištěný_text1.remove(slovo)
print(vyčištěný_text1)



text2 = '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''
text2_split = text2.split()
vyčištěný_text2 = []
for slovo in text2_split:
    vyčištěný_text2.append(slovo.strip(".,:;"))
for slovo in vyčištěný_text2:
  if slovo == "":
    vyčištěný_text1.remove(slovo)
print(vyčištěný_text1)


text3 = '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
text3_split = text3.split()
vyčištěný_text3 = []
for slovo in text3_split:
    vyčištěný_text3.append(slovo.strip(".,:;"))
for slovo in vyčištěný_text2:
  if slovo == "":
    vyčištěný_text1.remove(slovo)
print(vyčištěný_text1)


uživatelská_hesla = ["123", "pass123", "password123", "pass123"]
uživatelská_jména = ["bob", "ann", "mike", "liz"]
čísla_textů = ["1", "2", "3"]
zadané_jméno = input("Zadej své uživatelské jméno: ")
zadané_heslo = input("Zadej své heslo: ")



if zadané_jméno == uživatelská_jména[0] and zadané_heslo == uživatelská_hesla[0]:
    print(f"Ahoj {zadané_jméno}e. Vítej v našem textovém analzyátoru. ")
    výběr_textu = input("Vyber jeden z textů napsáním čísel 1, 2 nebo 3: ")   
elif zadané_jméno == uživatelská_jména[1] and zadané_heslo == uživatelská_hesla[1]:
    print(f"Ahoj {zadané_jméno}. Vítej v našem textovém analzyátoru. ")
    výběr_textu = input("Vyber jeden z textů napsáním čísel 1, 2 nebo 3: ")
elif zadané_jméno == uživatelská_jména[2] and zadané_heslo == uživatelská_hesla[2]:
    print(f"Ahoj {zadané_jméno[:3]}u. Vítej v našem textovém analzyátoru. ")
    výběr_textu = input("Vyber jeden z textů napsáním čísel 1, 2 nebo 3: ")   
elif zadané_jméno == uživatelská_jména[3] and zadané_heslo == uživatelská_hesla[3]:
    print(f"Ahoj {zadané_jméno}. Vítej v našem textovém analzyátoru. ")
    výběr_textu = input("Vyber jeden z textů napsáním čísel 1, 2 nebo 3: ")
else: 
    print(" Nesprávné jméno nebo heslo. Ukončuji program.")
    exit()

if výběr_textu not in čísla_textů:
        print(" Neplatný výběr textu. Ukončuji program")
        exit()
elif výběr_textu == čísla_textů[0]:

        počet_slov = len(vyčištěný_text1)
        počet_slov_s_velkým = []
        počet_velkých_slov = []
        počet_malých_slov = []
        počet_čísel = []
        
        
        for slovo in vyčištěný_text1:
            if slovo.istitle() == True:
              počet_slov_s_velkým.append(slovo)
            if slovo.isupper() == True:
              počet_velkých_slov.append(slovo)
            if slovo.islower() == True:
              počet_malých_slov.append(slovo)
            if slovo.isnumeric() == True:
              počet_čísel.append(int(slovo))
        
        výsledky = []
        délky_slov = []
        slovník_délek_a_počtu = {}
        for slovo in vyčištěný_text1:
          délky_slov.append(len(slovo))

        for čísla in sorted(délky_slov):
          slovník_délek_a_počtu[čísla] = délky_slov.count(čísla)


        for čísla in slovník_délek_a_počtu:
          výsledky.append((čísla,slovník_délek_a_počtu[čísla]))
        
        
elif výběr_textu == čísla_textů[1]:
        počet_slov = len(vyčištěný_text2)
        počet_slov_s_velkým = []
        počet_velkých_slov = []
        počet_malých_slov = []
        počet_čísel = []
        
        
        for slovo in vyčištěný_text2:
            if slovo.istitle() == True:
              počet_slov_s_velkým.append(slovo)
            if slovo.isupper() == True:
              počet_velkých_slov.append(slovo)
            if slovo.islower() == True:
              počet_malých_slov.append(slovo)
            if slovo.isnumeric() == True:
              počet_čísel.append(int(slovo))
        
        výsledky = []
        délky_slov = []
        slovník_délek_a_počtu = {}
        for slovo in vyčištěný_text2:
          délky_slov.append(len(slovo))

        for čísla in sorted(délky_slov):
          slovník_délek_a_počtu[čísla] = délky_slov.count(čísla)


        for čísla in slovník_délek_a_počtu:
          výsledky.append((čísla,slovník_délek_a_počtu[čísla])) 
        
elif výběr_textu == čísla_textů[2]:
        počet_slov = len(vyčištěný_text3)
        počet_slov_s_velkým = []
        počet_velkých_slov = []
        počet_malých_slov = []
        počet_čísel = []
        
        
        for slovo in vyčištěný_text3:
            if slovo.istitle() == True:
              počet_slov_s_velkým.append(slovo)
            if slovo.isupper() == True:
              počet_velkých_slov.append(slovo)
            if slovo.islower() == True:
              počet_malých_slov.append(slovo)
            if slovo.isnumeric() == True:
              počet_čísel.append(int(slovo))
        
        výsledky = []
        délky_slov = []
        slovník_délek_a_počtu = {}
        for slovo in vyčištěný_text3:
          délky_slov.append(len(slovo))

        for čísla in sorted(délky_slov):
          slovník_délek_a_počtu[čísla] = délky_slov.count(čísla)


        for čísla in slovník_délek_a_počtu:
          výsledky.append((čísla,slovník_délek_a_počtu[čísla])) 
        



        
        

print(f"Počet slov: {počet_slov}")
print(f"Počet slov s velkým počátečním písmenem: {len(počet_slov_s_velkým)}") 
print(f"Počet slov s velkýmy písmeny: {len(počet_velkých_slov)}") 
print(f"Počet slov s malými písmeny: {len(počet_malých_slov)}") 
print(f"Počet čísel: {len(počet_čísel)}")
print(f"Suma čísel: {sum(počet_čísel)}")
délka = "DÉLKA|"
výskyt = "VÝSKYT"
print(f"{délka: ^5} {výskyt: ^18}|POČET")
# ty seznamy jsou pro velikost mezer 
for dvojice in výsledky:
       hvězdička = "*" * dvojice[1]
       print(f"{(dvojice[0]): ^5}| {hvězdička: ^18}|{dvojice[1]}")
